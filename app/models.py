from django.db import models

# Create your models here.

from django.db import models

# Create your models here.


class Book(models.Model):
    artwork = models.URLField(max_length=255)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, related_name='books')

    def __str__(self):
        return self.title
