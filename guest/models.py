from django.db import models

class Student(models.Model):
	rno=models.CharField(max_length=10)
	sname=models.CharField(max_length=10)
	branch=models.CharField(max_length=10)
	fees=models.IntegerField()
	def __str__(self):
          return self.rno+" "+self.sname+" "+self.branch+" "+str(self.fees)
