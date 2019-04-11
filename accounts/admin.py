# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from accounts.models import UserProfile
# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'hint')


    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-phone', 'user')
        return queryset

admin.site.register(UserProfile, UserProfileAdmin)
