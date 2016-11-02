from django.contrib import admin
from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from .models import  *

@admin.register(Study)
class StudyAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">assignment_ind</i>'

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">local_hospital</i>'


# Register your models here.
admin.site.register(CancerCase)
admin.site.register(ClipsCase)
admin.site.register(ObservationalCase)
admin.site.register(ObsinternationalCase)

#Delete this line to let clips_app to take over the users
admin.site.unregister(User)

class UserProfileInline(admin.StackedInline):
    model = UserProfile

class UserProfileAdmin(UserAdmin):
    inlines = [UserProfileInline]

#Delete this line to let clips_app to take over the users
admin.site.register(User, UserProfileAdmin)
