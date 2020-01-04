from django.contrib import admin

# Register your models here.

from .models import todoitem

admin.site.register(todoitem)