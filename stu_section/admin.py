from django.contrib import admin

from . import models
from .models import Student

# Register your models here.
admin.site.register(Student)

