from django.db import models

class Register(models.Model):  #Register is Model class
  email= models.CharField(max_length=20)
  password=models.CharField(max_length=10)
  mobile=models.CharField(max_length=12)
  fullname=models.CharField(max_length=50)

  

