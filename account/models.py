from django.db import models


class User(models.Model):
    name = models.CharField(max_length=512)
    email = models.EmailField(unique=True)
    timeCreation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'
