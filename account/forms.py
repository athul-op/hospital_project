from  django import forms
from . models import Account
from django.forms import fields 
from superadmin.models import *

class RegistrationForm(forms.ModelForm):


    password=forms.CharField(widget=forms.PasswordInput)
    confirm_password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=Account
        fields=['first_name','last_name','email','mobile','password']

    def _init_(self,*args,**kwargs):
        super(RegistrationForm ,self)._init_(*args,**kwargs)  
       
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'
        

    # def _init_(self, *args, **kwargs):
    #     super()._init_(*args, **kwargs)
    #     self.fields.pop('password','confirm_password')



class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['first_name','email','mobile','message','selectdoctor','selectdoctor']

    def _init_(self,*args,**kwargs):
        super(AppointmentForm ,self)._init_(*args,**kwargs)  
       
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'
