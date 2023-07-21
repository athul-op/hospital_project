from django.db import models

# Create your models here.

class Doctor(models.Model):
    
    name = models.CharField(max_length=20)
    availabledate=models.DateField(auto_now_add=False)
    availabletime=models.TimeField(auto_now_add=False)
    profile_pic=models.ImageField(upload_to='media',null=True,blank=True)
    mobile=models.CharField(max_length=20,null=True)
    department=models.CharField(max_length=50)
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.name
    

class DoctorGallery(models.Model):
    Doctor = models.ForeignKey(Doctor,default=None,on_delete=models.CASCADE)
    def __str__(self):
        return self.Doctor.name

