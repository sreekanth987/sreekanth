from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(register)
admin.site.register(newevent)
admin.site.register(booked)
admin.site.register(contact_1)
admin.site.register(PasswordReset)
admin.site.register(book_1)