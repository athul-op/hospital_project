from django.shortcuts import render
from django .contrib import messages,auth
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from.models import Doctor,DoctorGallery
from account.models import Account
from account . forms import RegistrationForm
from .forms import DoctorForm
# Create your views here.


def master_signin(request):


    if request.method == "POST":

        name = request.POST["name"]
        password = request.POST["password"]
        print(name,password)
        
        user = auth.authenticate(username=name,password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "Login Successful")
            return redirect("admin_home")
        else:
            messages.error(request, "Invalid credentials")
            return redirect("admin_login")

    else:
        return render(request, "admin_login.html")


# @login_required(login_url='admin_signin')
def admin_home(request):

    count=Doctor.objects.count()
    patient_count=Account.objects.count()
    context={
        'count':count,
        'patient_count':patient_count,
    }  
    return render (request,'admin/admindash.html',context)
    
   
    
def doctor_details(request):
    if request.user.is_authenticated:
        users= Doctor.objects.all()
        context = {'users':users}
        return render(request,'admin/doctor_details.html',context)
    else:
        return redirect("admin_home")
    
def patient_details(request):
    if request.user.is_authenticated:
        order= Account.objects.all()
        
        context ={'order':order,}
        return render(request,'admin/patient_details.html',context)
    else:
        return redirect("admin_home")
    



def add_doctors(request):
    if request.method == "POST":
        form = DoctorForm(request.POST,request.FILES)
        if form.is_valid():          
            form.save()
            return redirect('admin_home') 
        else:
            print('not added')
            messages.info(request,'not added')
    else:
        form = DoctorForm()
    return render(request,'admin/add_product.html',{'form':form})

# def doctors_edit(request,id):
#     item =Doctor.objects.get(id=id)
#     # in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request),product=item).exists()
#     doctor_gallery = DoctorGallery.objects.filter(Doctor_id=item.id)  
    
#     context = {
#         'items': item,
#         # 'in_cart':in_cart,
#         # 'doctor_gallery':doctor_gallery,
#     }
#     return render(request,'admin/doctor_edit.html',context)    

def doctors_edit(request,id):
    item =Doctor.objects.get(id=id)
    if request.method == "POST":
        form = DoctorForm(request.POST,request.FILES,instance=item)
        if form.is_valid():          
            form.save()
            return redirect('admin_home') 
        else:
            print('not added')
            messages.info(request,'not added')
    
    form = DoctorForm(instance=item)
    context={'form' :form}
    return render(request,'admin/doctor_edit.html',context)
 






def edit_patient(request,id):
    item =Account.objects.get(id=id)
    if request.method == "POST":
        form = RegistrationForm(request.POST,request.FILES,instance=item)
        if form.is_valid():          
            form.save()
            return redirect('admin_home') 
        else:
            print('not added')
            messages.info(request,'not added')
    
    form = RegistrationForm(instance=item)
    context={'form' :form}
    return render(request,'admin/patient_edit.html',context)


def delete_doctor(request,id):
        adminprod =  Doctor.objects.get(id=id)
        adminprod.delete()
        return redirect('admin/patient_edit.html')

    

def admin_logouts(request):
    
    if request.user:

        auth.logout(request)
        return redirect(master_signin)
    else:
        return redirect("admin_home")    