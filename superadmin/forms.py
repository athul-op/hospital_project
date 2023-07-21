from  django import forms
from django.forms import fields    
# from . models import Account
from .models import *


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name','availabledate','availabletime','profile_pic','mobile','department']


    def __init__(self,*args,**kwargs):
        super(DoctorForm,self).__init__(*args,**kwargs)    

        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'    

            