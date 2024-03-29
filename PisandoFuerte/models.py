from django.db import models
from django.contrib.auth.models import User

class Nike(models.Model):
    modelo= models.CharField(max_length=50)
    talle= models.IntegerField()
    
    def __str__(self):
        return f"{self.modelo}"
    
    class Meta:
        ordering = ["modelo"]
    
class Adidas(models.Model):
    modelo=models.CharField(max_length=50)
    talle=models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.modelo}"
    
    class Meta:
        ordering = ["modelo"]
    
class Puma(models.Model):
   modelo=models.CharField(max_length=50)
   talle=models.CharField(max_length=50) 
   
   def __str__(self):
        return f"{self.modelo}" 
    
class Meta:
    ordering = ["modelo"]
    
   
class Remeras(models.Model):
    color=models.CharField(max_length=50)
    talle=models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.color}"
    
    class Meta:
        ordering = ["color"]
        
class Avatar(models.Model):
    imagen= models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user}{self.imagen}"
    

    
    

    

