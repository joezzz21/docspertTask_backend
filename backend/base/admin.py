from django.contrib import admin

# Register your models here.

from .models import User, Book, Page

admin.site.register([User, Book, Page])
