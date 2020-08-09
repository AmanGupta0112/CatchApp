from django.shortcuts import render
from .forms import ProfileForm,UserCreateForm
from django.views import generic
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .models import Profile
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
# Create your views here.
User = get_user_model()
class SignUp(generic.CreateView):

    form_class = UserCreateForm
    success_url = reverse_lazy('accounts:profile')
    template_name = 'accounts/signup.html'

class ProfileView(LoginRequiredMixin,generic.CreateView):

    form_class = ProfileForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/profile.html'

class UpdateProfile(LoginRequiredMixin,generic.UpdateView):
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/profile.html'
