from django.db import models

class Category(models.Model):  #Register is Model class
  catname= models.CharField(max_length=20)
class Subcategory(models.Model):  #Register is Model class
  subcatname= models.CharField(max_length=20)
  catid= models.IntegerField()
class Product(models.Model):
 productname=models.CharField(max_length=20)
 proddesc=models.CharField(max_length=50)
 subcatid=models.IntegerField()	
 create_date = models.DateTimeField()



  