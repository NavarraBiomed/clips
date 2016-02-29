from django.contrib import admin
from django import forms
from django.db import models
# Register your models here.

from .models import Study, Hospital

class StudyAdmin(admin.ModelAdmin):
	
    formfield_overrides = {
        models.IntegerField: {'widget': forms.NumberInput},
    }
    

admin.site.register(Hospital)
admin.site.register(Study, StudyAdmin)