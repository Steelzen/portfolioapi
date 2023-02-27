from django.db import models

# Create your models here.
class AboutMe(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    summary = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=50)
    content = models.CharField(max_length=300)
    img_src = models.URLField(max_length=300, default="")
    site_link = models.URLField(max_length=300, default="")
    code_link = models.URLField(max_length=300, default="")
    
    def __str__(self):
        return self.name      
