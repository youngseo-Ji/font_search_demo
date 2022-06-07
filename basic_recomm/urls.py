from django.urls import path

from . import views

app_name="basic_recomm"

urlpatterns = [
    path('', views.index),
    path('search_font/', views.search_font, name='search_font')
]