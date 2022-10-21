"""App_novation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from patient import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('patient/', views.Patient_home, name='home_patient'),
    path('Doctor/', views.Doctor_home, name='home_doc'),
    path('MyData/', views.Data, name="Data"),
    path('AddFile/', views.Add_File.as_view(), name="AddFile"),
    # AUTH
    path('signup', views.SignUp, name='signup'),
    path('signup/patient/', views.PaitentSignUpView.as_view(), name='Patient_signup'),
    path('signup/Doctor/', views.DoctorSignUpView.as_view(), name='Doctor_signup'),
    path('login', views.loginuser, name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('password/', auth_views.PasswordChangeView.as_view(template_name = "registration/change_password.html"), name="password_change"),
    # ACCOUNT
    path('patient/MyProfile', views.Patient_Profile.as_view(), name='Personal_Patient_Profile'),
    path('Doctor/MyProfile', views.Doctor_Profile.as_view(), name='Personal_Doctor_Profile'),
    #DOCTOR

]
