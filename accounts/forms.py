
from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from accounts.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
import psycopg2



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)
    hint = forms.CharField(required=True)
    class Meta():
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'phone',
            'hint'

        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']
        user.hint = self.cleaned_data['hint']

        if commit:
            user.save()

        return user

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)
    hint = forms.CharField(required=True)
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password',
            'phone',
            'hint'
        )
