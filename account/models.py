from django.db import models
from superadmin.models import *
class Account(models.Model):
    first_name   = models.CharField(max_length=100,null=True)
    last_name     = models.CharField(max_length=100,null=True)  
    email         = models.EmailField(max_length=100,unique=True)
    mobile        = models.CharField(max_length=10,unique=True,null=True)
    # date_of_birth =  models.BigIntegerField()
    # patient_id    = models.BigIntegerField()
    password     =models.CharField(max_length=100,null=True) 
    message =models.CharField(max_length=100,null=True)
    selectdoctor =models.ForeignKey(Doctor,on_delete=models.CASCADE,null=True)
    
    def __str__(self):

       return self.email
    

class Service(models.Model):
    heading = models.CharField(max_length=100,null=True)
    content = models.TextField(max_length=1000,null=True)
    image=models.ImageField(upload_to='media',null=True,blank=True)
    subheading=models.CharField(max_length=100,null=True)
    id       = models.AutoField(db_index=True,primary_key=True,null=False)

    # def __str__(self):
    #     return self.heading

class Service_1(models.Model):
    heading = models.CharField(max_length=100,null=True)
    content = models.TextField(max_length=1000,null=True)
    image=models.ImageField(upload_to='media',null=True,blank=True)
    subheading=models.CharField(max_length=100,null=True)
    id       = models.AutoField(db_index=True,primary_key=True,null=False)


class Service_2(models.Model):
    heading = models.CharField(max_length=100,null=True)
    content = models.TextField(max_length=1000,null=True)
    image=models.ImageField(upload_to='media',null=True,blank=True)
    subheading=models.CharField(max_length=100,null=True)
    id       = models.AutoField(db_index=True,primary_key=True,null=False)    


class Service_3(models.Model):
    heading = models.CharField(max_length=100,null=True)
    content = models.TextField(max_length=1000,null=True)
    image=models.ImageField(upload_to='media',null=True,blank=True)
    subheading=models.CharField(max_length=100,null=True)
    id       = models.AutoField(db_index=True,primary_key=True,null=False)        


class Service_4(models.Model):
    heading = models.CharField(max_length=100,null=True)
    content = models.TextField(max_length=1000,null=True)
    image=models.ImageField(upload_to='media',null=True,blank=True)
    subheading=models.CharField(max_length=100,null=True)
    id       = models.AutoField(db_index=True,primary_key=True,null=False)            