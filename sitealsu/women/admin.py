from django.contrib import admin

from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'sex', 'email', 'phone', 'birthday', 'cat', 'time_created')
    list_display_links = ('id', 'first_name')
    ordering = ['id']


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', )
    ordering = ['id']



