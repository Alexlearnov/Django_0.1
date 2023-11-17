from django.db import models
from django.urls import reverse


class User(models.Model):
    class Sex(models.IntegerChoices):
        male = 1, 'male'
        female = 0, 'female'

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, db_index=True, unique=True)
    sex = models.BooleanField(choices=Sex.choices)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=20, unique=True)
    birthday = models.DateField()
    time_created = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.slug}, " \
               f"time_created={self.time_created}, birthday={self.birthday}"

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name



class Courses(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, db_index=True, blank=True, default='')

    short_description = models.TextField(max_length=1000)

    price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f"{self.name}, {self.slug}, {self.price}"

    def get_absolute_url(self):
        return reverse("course", kwargs={"course_slug": self.slug})






