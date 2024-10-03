from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profil, Reponse


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email',
                  'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfilUpdateForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ['image', 'bio', 'competence',
                  'github', 'linkedin']


class ReponseForm(forms.ModelForm):
    class Meta:
        model = Reponse
        fields = ['champ_reponse']
