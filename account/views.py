from django.shortcuts import redirect, render

from django.shortcuts import render

from.models import Account
from.models import Service,Service_1,Service_2,Service_3,Service_4
from . forms import  RegistrationForm
from django.contrib.auth import authenticate
from django .contrib import messages,auth
from . forms import  AppointmentForm
import random
from django.core.mail import send_mail,EmailMessage
from otplogin.models import OTP

# Create your views here.




from django.contrib.auth import login
from django.shortcuts import redirect

def register(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print('form created')


        if form.is_valid():
            print('form valid')
            first_name = form.cleaned_data['first_name']
            last_name  = form.cleaned_data['last_name']
            email      = form.cleaned_data['email']
            mobile     = form.cleaned_data['mobile']
            password   = form.cleaned_data['password']

            print(first_name,last_name,email)

            user = Account(
                first_name=first_name,
                last_name =last_name,
                email     =email,
                mobile    =mobile,
                password  =password,
            )
            
            user.save()
        


    form = RegistrationForm()
    context = { 'form' : form }
    return render(request,'signup.html',context)  
   



# def user_login(request):   
#       return render(request,'login.html')


def user_login(request):

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":

        email = request.POST["email"]
        password = request.POST["password"]
        
        user = auth.authenticate(email=email,password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "Login Successful")
            return redirect("user_login")
        else:
            messages.error(request, "Invalid credentials")
            return redirect("home")

    else:
        return render(request, "login.html")





def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def gallery(request):
    return render(request,'gallery.html')

def team(request):
    return render(request,'team.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

def appoinment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST,request.FILES)
        if form.is_valid():          
            form.save()
            return redirect('home') 
        else:
            print('not added')
            messages.info(request,'not added')
    else:
        form = AppointmentForm()
    return render(request,'appointment.html',{'form':form})

# def service(request):
#     eye= Service.objects.filter(heading='heading')
#     return render(request,'service_1.html',{'eye':eye})


def service(request):
    eye= Service.objects.all()
    return render(request,'service_1.html',{'eye':eye})

def service_1(request):
    item= Service_1.objects.all()
    return render(request,'service_2.html',{'item':item})

def service_2(request):
    item= Service_2.objects.all()
    return render(request,'service_3.html',{'item':item})

def service_3(request):
    item= Service_3.objects.all()
    return render(request,'service_4.html',{'item':item})

def service_4(request):
    item= Service_4.objects.all()
    return render(request,'service_5.html',{'item':item})











def log(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        token = str(random.randint(100000,999999))
        OTP.objects.update_or_create(email=email, defaults={'token':token})

        send_mail(
            'OTP for Login',
            f'Your OTP is: {token}',
            'lothbrok007007@gmail.com',
            [email],
            fail_silently=False,
        )
        return render(request,'otp/otp_verification.html',{'email':email})
    return render(request,'otp/send_otp.html')




def verify_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        otp = request.POST.get('otp')
        otp_obj = OTP.objects.filter(email=email, token=otp).order_by('created_at').first()
        if otp_obj:
            otp_obj.delete()
            return redirect('doctor_details')
        else:
            messages.error(request, "Incorrect OTP") 
    return redirect('log_in')    


