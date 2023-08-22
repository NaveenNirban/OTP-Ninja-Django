from django.contrib import admin
from .models import Projects, OtpMaster, MyUser


# Register your models here.

admin.site.register(Projects)
admin.site.register(OtpMaster)
admin.site.register(MyUser)