from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120)
    price = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products', null=True)

    def __str__(self):
        return self.name
