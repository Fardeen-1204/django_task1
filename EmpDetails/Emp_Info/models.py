from django.db import models

# Create your models here.
class EmpDetails(models.Model):
    emp_name=models.CharField(max_length=50)
    emp_city=models.CharField(max_length=50)
    emp_company=models.CharField(max_length=50)
    descriptions=models.TextField(max_length=500,null =True)
    emp_photo=models.ImageField(upload_to='images/')
    def __str__(self):
       return f"{self.emp_name}"