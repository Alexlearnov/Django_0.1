from django.contrib import admin

from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'first_name', 'last_name', 'sex', 'email', 'phone', 'birthday', 'cat', 'time_created', 'brief_info')
    list_display_links = ('id', 'first_name')
    ordering = ['id']

    @admin.display(description='Описание')
    def brief_info(self, user: models.User):
        return f"Описание {user.first_name} пользователя"

    @admin.action(description="Сменить пол на женский")
    def set_sex(self, request, queryset):
        count = queryset.update(sex=models.User.Sex.female)
        self.message_user(request, f"Изменено {count} записи(ей)", messages.WARNING)

    actions = ['set_sex']


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
    ordering = ['id']
