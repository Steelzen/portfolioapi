from django.db import models

# Create your models here.
class AboutMe(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    summary = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name
