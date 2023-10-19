from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    sex = models.CharField(max_length=6)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    birthday = models.DateField()
    time_created = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.email}, " \
               f"time_created={self.time_created}, birthday={self.birthday}"

