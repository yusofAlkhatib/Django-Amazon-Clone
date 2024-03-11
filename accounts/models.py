from django.db import models
from django.contrib.auth.models import User


# Create your models here.


ADDRESS_TYPE = (
    ('Home' , 'Home') ,
    ('office' , 'Office') ,
    ('Bussines' , 'Bussines',) ,
    ('Other' , 'Other') ,
)


class Address(models.Model):
    user = models.ForeignKey(User,related_name='user_address',on_delete=models.CASCADE)
    address = models.TextField(max_length=300)
    type = models.CharField(max_length=20,choices=ADDRESS_TYPE)