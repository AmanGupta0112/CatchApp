from django import  forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class UserCreateForm(UserCreationForm):

    class Meta():
        fields = ('username','email','password1','password2')
        model = User

class  ProfileForm(forms.ModelForm):

    class Meta():
        model = Profile
        fields = "__all__"
