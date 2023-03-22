from django.contrib import admin
from .models import Motor,Current,Voltage

# Register your models here.
admin.site.register(Motor)
admin.site.register(Current)
admin.site.register(Voltage)