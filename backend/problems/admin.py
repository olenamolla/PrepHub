from django.contrib import admin
from .models import Problem

# Register your models here.

# making models accesible in the admin panel so I can add/view problems easily
admin.site.register(Problem)