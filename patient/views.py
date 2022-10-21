from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView, ListView, UpdateView
from .forms import Updateprofile, PatientSignUpForm, DoctorSignUpForm, Add_file
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator
from .decoraters import Patient_required, Doctor_required
from django.contrib.auth.forms import AuthenticationForm
from .models import Prescription


def home(request):
    try:
        if request.user.is_Doctor:
            return redirect('home_doc')
        elif request.user.is_Patient:
            return redirect("home_patient")
    except:
        return render(request, "patient/base.html")


@login_required
@Patient_required
def Patient_home(request):
    User = request.user
    return render(request, 'patient/home.html', {User: "user"})


@login_required
@Doctor_required
def Doctor_home(request):
    return render(request, 'patient/home_doc.html', )


def SignUp(request):
    return render(request, 'registration/Signup_as.html')


@method_decorator([login_required, Patient_required], name="dispatch")
class Patient_Profile(generic.UpdateView):
    form_class = Updateprofile
    template_name = "patient/profile.html"
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class PaitentSignUpView(CreateView):
    model = get_user_model()
    form_class = PatientSignUpForm
    template_name = 'registration/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'patient'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class DoctorSignUpView(CreateView):
    model = get_user_model()
    form_class = DoctorSignUpForm
    template_name = 'registration/signup_doc.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Doctor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home_doc')


@method_decorator([login_required, Doctor_required], name="dispatch")
class Doctor_Profile(generic.UpdateView):
    form_class = Updateprofile
    template_name = "patient/profile_doc.html"
    success_url = reverse_lazy('home_doc')

    def get_object(self):
        return self.request.user


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'registration/login.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'registration/login.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            if request.user.is_Doctor:
                return redirect('home_doc')
            else:
                return redirect('home')


@login_required
@Patient_required
def Data(request):
    object_list = Prescription.objects.filter(user= request.user)
    return render(request, "patient/Data.html" , {'object_list': object_list})



@method_decorator([login_required, Patient_required], name="dispatch")
class Add_File(LoginRequiredMixin, generic.CreateView):
    form_class = Add_file
    template_name = 'patient/Add_file.html'
    success_url = reverse_lazy('Data')

    def form_valid(self, form):
        form.instance.user = self.request.user
        super(Add_File, self).form_valid(form)
        return redirect('Data')