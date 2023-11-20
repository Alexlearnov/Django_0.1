from django.db import models
from django.urls import reverse


class User(models.Model):
    class Sex(models.IntegerChoices):
        male = 1, 'male'
        female = 0, 'female'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    slug = models.SlugField(max_length=255, db_index=True, unique=True)
    sex = models.BooleanField(choices=Sex.choices, verbose_name='Пол')
    email = models.EmailField(max_length=255, unique=True, verbose_name='Мыло')
    phone = models.CharField(max_length=20, unique=True, verbose_name='Телефон')
    birthday = models.DateField(verbose_name='День рождения')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='УЗ создана')
    time_update = models.DateTimeField(auto_now=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категории')

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.slug}, " \
               f"time_created={self.time_created}, birthday={self.birthday}"

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True)



    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории женщин"

    def get_absolute_url(self):
        return reverse("category", kwargs={"category_slug": self.slug})

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






