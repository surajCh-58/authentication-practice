from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    gender_choices=[('M','Male'),('F','Female'),('O','Other')]
    gender=models.CharField(choices=gender_choices,max_length=1)
    phone=models.CharField(max_length=13)

    def __str__(self):
        self.user.username