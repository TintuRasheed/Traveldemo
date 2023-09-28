from django.db import models

# Create your models here.
class Place(models.Model):
    Name=models.CharField(max_length=250)
    Img=models.ImageField(upload_to='Pics')
    Desc=models.TextField()
    
    def __str__(self):
        return self.Name
    
    
class Person(models.Model):
    Pic=models.ImageField(upload_to='Pics')
    Name=models.CharField(max_length=20)
    Dis=models.TextField()
    
    def __str__(self):
        return self.Name