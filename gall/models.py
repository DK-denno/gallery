from django.db import models

# Create your models here.


class Location(models.Model):
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.location
   

class Category(models.Model):
    category = models.CharField(max_length=10)

    
    def __str__(self):
        return self.category


class Posts(models.Model):
    name = models.CharField(max_length=50)
    caption = models.CharField(max_length = 50)
    description = models.CharField(max_length=50)
    article_image = models.ImageField(upload_to = 'articles/')
    location = models.ManyToManyField(Location)
    category = models.ManyToManyField(Category)
    
    def __str__(self):
        return self.name