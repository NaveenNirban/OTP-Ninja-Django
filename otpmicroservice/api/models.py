from django.db import models
import uuid
from django.contrib.auth import get_user_model
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, AbstractUser
)

class Projects(models.Model):
    name = models.CharField(max_length=255)
    apiKey = models.UUIDField(default=uuid.uuid4)
    quota = models.IntegerField(default=0)
    logo = models.URLField(null=True,blank=True)
    otpCounter = models.IntegerField(default=0,verbose_name='OTP Counter')
    class Meta:
        verbose_name_plural = "Projects"
    def __str__(self):
        return str(self.name)

class MyUser(AbstractUser):
    project = models.ForeignKey(Projects,on_delete=models.CASCADE,blank=True,null=True)

    ### Remove this line when to create admin from console.
    # def save(self, *args, **kwargs):
    #     # Hash the password if it's provided
    #     if self.password:
    #         self.set_password(self.password)
    #     super().save(*args, **kwargs)
    

class OtpMaster(models.Model):
    otp = models.CharField(max_length=10,blank=True,null=True)
    project = models.ForeignKey(Projects,on_delete=models.CASCADE)
    email = models.CharField(max_length=100,blank=True,null=True)
    class Meta:
        verbose_name_plural = "Otp Master"
    def __str__(self):
        return str(self.project.name)+" - "+str(self.email)