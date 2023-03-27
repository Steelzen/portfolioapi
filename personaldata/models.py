from django.db import models

# Create your models here.
class AboutMe(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    site = models.URLField(max_length=300, default="")
    github = models.URLField(max_length=300, default="")
    summary = models.CharField(max_length=500, default="")
    photo_src = models.URLField(max_length=300, default="")
    introductory = models.CharField(max_length=500, default="")
    title_img_src = models.URLField(max_length=300, default="")
    additional_info = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=50)
    content = models.CharField(max_length=500, default="")
    img_src = models.URLField(max_length=300, default="")
    site_link = models.URLField(max_length=300, default="")
    code_link = models.URLField(max_length=300, default="")
    video_link = models.URLField(max_length=300, default="")
    additional_info = models.CharField(max_length=500, default="")
    
    def __str__(self):
        return self.name      
