from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=230)
    subtitle = models.CharField(max_length=240)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title
