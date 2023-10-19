from django import template
from women import views

register = template.Library()

cats_db = [
    {'id': 1, 'name': 'Актрисы'},
    {'id': 2, 'name': 'Певицы'},
    {'id': 3, 'name': 'Спортсменки'},
]

@register.simple_tag()
def get_categories():
    return cats_db



