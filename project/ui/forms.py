from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from ui.models import Homes


class CreateAdminUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']


class CreateHome(forms.ModelForm):

    class Meta:
        model = Homes
        fields = '__all__'
        exclude = ['type']

