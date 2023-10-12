from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index),
    re_path(r'^archive/(?P<year>[0-9]{4})/', views.archive),
    path('edit/<slug:slug>/', views.update_page, name='edit_page'),
]


