# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser, UserManager

from django.db import models, migrations
from django.contrib.auth.models import User, AbstractUser, UserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
import psycopg2

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    phone = models.CharField(max_length=10, default='')
    hint = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
