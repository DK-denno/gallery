from django.db import models

# Create your models here.


class Location(models.Model):
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.location
   

class Category(models.Model):
    name = models.CharField(max_length=10)

    
    def __str__(self):
        return self.name


class Posts(models.Model):
    name = models.CharField(max_length=50)
    caption = models.CharField(max_length = 50)
    description = models.CharField(max_length=50)
    article_image = models.ImageField(upload_to = 'articles/')
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    
    def __str__(self):
        return self.name