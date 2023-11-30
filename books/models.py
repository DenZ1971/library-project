from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=512)
    year = models.IntegerField()
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return f'{self.title}'
