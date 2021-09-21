from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Movie(models.Model):
    name = models.CharField(max_length=32, unique=True)
    language = models.CharField(max_length=16)


class City(models.Model):
    name = models.CharField(max_length=32, unique=True)


class Theatre(models.Model):
    name = models.CharField(max_length=32, unique=True)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)


class Show(models.Model):
    name = models.CharField(max_length=32)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    total_seats = models.IntegerField(default=100)
    available_seats = models.IntegerField(default=100)


class Mapping(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.DO_NOTHING)
    theatre = models.ForeignKey(Theatre, on_delete=models.DO_NOTHING)
    show = models.ForeignKey(Show, on_delete=models.DO_NOTHING)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
