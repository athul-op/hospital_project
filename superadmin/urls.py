from django.urls import path
from .import views

urlpatterns = [
path('admin_home/',views.admin_home,name="admin_home"),
path('',views.master_signin,name="admin_login"),
path('doctor_details/',views.doctor_details,name='doctor_details'),
path('patient_details/',views.patient_details,name='patient_details'),
path('doctors_edit/<str:id>/',views.doctors_edit,name="doctors_edit"),
path('add_doctor/',views.add_doctors,name="add_doctor"),
path('edit_patient/<int:id>',views.edit_patient,name='edit_patient'),
path('delete_doctor/<int:id>',views.delete_doctor,name="delete_doctor"),
path('admin_logout',views.admin_logouts,name='admin_logout'),

] 