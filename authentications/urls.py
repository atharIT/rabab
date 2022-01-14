from django.contrib import admin
from django.contrib import auth
from django.urls import path
from . import views

app_name = "authentications"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('volunteerRegister/', views.volunteerRegister, name='volunteerRegister'),
    path('superviorRegister/', views.superviorRegister, name='superviorRegister'),
    path('adminRegister/', views.adminRegister, name='adminRegister'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),

]
