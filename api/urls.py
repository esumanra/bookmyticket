from django.urls import path
from . import views

urlpatterns = [
    path("movies/<str:city>", views.list_movies_by_city),
    path("shows/<movie_name>/<city_name>", views.list_shows_for_movie),
    path("book", views.book_ticket),
]
