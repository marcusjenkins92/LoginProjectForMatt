# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import psycopg2
from django.shortcuts import render, redirect
from accounts.models import UserProfile
from accounts.forms import (
     RegistrationForm,
     EditProfileForm
 )
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse

# Create your views here.

def home(request):
    return render(request, 'accounts/home.html')

def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()
            user.hint = user_form.cleaned_data.get('hint')
            user.phone = user_form.cleaned_data.get('phone')
            user.save()
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect(reverse('accounts:home'))
    else:
        user_form = RegistrationForm()
    return render(request,'accounts/reg_form.html',
                          {'user_form':user_form})


def profile(request):
    args ={'user': request.user}
    return render(request, 'accounts/profile.html', args)

def edit_profile(request):
    if request.method =='POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid:
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('accounts:profile')
        else:
            return redirect('accounts:change-password')

    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)
