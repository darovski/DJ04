from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('films', views.film, name='films'),
    path('comment', views.create_comment_films, name='comment')
]