from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)

from .models import *
from .serializers import *

import logging

# file handler defined in settings.py
logger = logging.getLogger(__name__)


@api_view(["GET"])
def getRoutes(request):

    routes = [
        {
            "Endpoint": "/movies/<city>",
            "method": "GET",
            "body": None,
            "description": "Return the movies in the city",
        },
        {
            "Endpoint": "shows/<movie_name>/<city_name>",
            "method": "GET",
            "body": None,
            "description": "Return the shows playing in the city for a movie",
        },
        {
            "Endpoint": "/book",
            "method": "POST",
            "authorization header": "Token <token-value>",
            "body": {
                "city_name": "city_name",
                "movie_name": "movie_name",
                "theatre_name": "theatre_name",
                "show_name": "show_name",
                "ticket_nos": "ticket_nos",
            },
            "description": "Book a ticket for a show in a theatre",
        },
        {
            "Endpoint": "/dj-rest-auth/login/",
            "method": "POST",
            "body": {"username": "username", "password": "password"},
            "description": "Login",
        },
        {
            "Endpoint": "/dj-rest-auth/logout/",
            "method": "POST",
            "body": None,
            "description": "Logout",
        },
        {
            "Endpoint": "/dj-rest-auth/registration/",
            "method": "POST",
            "body": {
                "username": "username",
                "password1": "password",
                "password2": "password",
            },
            "description": "User registration",
        },
    ]
    return Response(routes)


@api_view(["GET"])
def list_movies_by_city(request, city):
    city_name = city.title()
    requested_city = City.objects.filter(name=city_name).first()
    if requested_city:
        movies_in_requested_city = (
            Mapping.objects.filter(city=requested_city).values("movie_id").distinct()
        )
        movies_list_json = []
        for movie_in_requested_city in movies_in_requested_city:
            movies = Movie.objects.filter(pk=movie_in_requested_city["movie_id"])
            for movie in movies:
                movies_list_json.append(MovieSerializer(movie).data)
        return JsonResponse(movies_list_json, safe=False)
    else:
        logger.info("`%s` city is not availabe", city_name)
        return JsonResponse(
            {"message": "Currently %s is not registered in our cities" % city_name}
        )


def get_theatre_shows_mapping(theatre_show_list):
    theatre_shows_map = [
        {
            "theatre_id": id,
            "show_id": [
                d["show_id"] for d in theatre_show_list if d["theatre_id"] == id
            ],
        }
        for id in set(map(lambda d: d["theatre_id"], theatre_show_list))
    ]
    theatres_list = []
    for theatre_show in theatre_shows_map:
        theatre = Theatre.objects.filter(pk=theatre_show["theatre_id"]).first()
        theatre_shows_json = TheatreSerializer(theatre).data
        shows_list_json = []
        for show_id in theatre_show["show_id"]:
            show = Show.objects.filter(pk=show_id).first()
            shows_list_json.append(ShowSerializer(show).data)
        theatre_shows_json["shows"] = shows_list_json
        theatres_list.append(theatre_shows_json)
    return theatres_list


@api_view(["GET"])
def list_shows_for_movie(request, movie_name, city_name):
    movie_name = movie_name.title()
    city_name = city_name.title()
    requested_city = City.objects.filter(name=city_name).first()
    requested_movie = Movie.objects.filter(name=movie_name).first()
    if requested_city and requested_movie:
        shows_for_requested_movie_in_city = Mapping.objects.filter(
            city=requested_city, movie=requested_movie
        ).values("show_id", "theatre_id")
        theatre_show_list = list(shows_for_requested_movie_in_city)
        theatre_shows_json = get_theatre_shows_mapping(theatre_show_list)
        movie_details_json = MovieSerializer(requested_movie).data
        movie_details_json["theatres"] = theatre_shows_json
        return JsonResponse(movie_details_json, safe=False)
    elif requested_city is None:
        logger.info("`%s` city is not available", city_name)
        return JsonResponse({"message": "%s city not available" % city_name})
    elif requested_movie is None:
        return JsonResponse({"message": "%s movie is not available" % movie_name})


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def book_ticket(request):
    try:
        city_name = request.POST["city_name"]
        movie_name = request.POST["movie_name"]
        theatre_name = request.POST["theatre_name"]
        show_name = request.POST["show_name"]
        ticket_nos = int(request.POST["ticket_nos"])
    except:
        return JsonResponse({"message": "Not enough details to book the ticket"})
    if not ticket_nos:
        return JsonResponse({"message": "Cannot book '0' tickets"})
    city = City.objects.filter(name__iexact=city_name).first()
    movie = Movie.objects.filter(name__iexact=movie_name).first()
    theatre = Theatre.objects.filter(name__iexact=theatre_name).first()
    show = Show.objects.filter(name__iexact=show_name).first()
    movie_show = Mapping.objects.filter(
        city=city, movie=movie, theatre=theatre, show=show
    ).first()
    if movie_show:
        if movie_show.show.available_seats >= 1:
            movie_show.show.available_seats -= 1
            movie_show.show.save()
            return JsonResponse(
                {"message": "You have successfully booked ticket for this show"}
            )
        else:
            logger.info("")
            return JsonResponse({"message": "House Full"})
    else:
        logger.error(
            "The requested show cannot be booked `%s %s %s %s`",
            city_name,
            movie_name,
            theatre_name,
            show_name,
        )
        return JsonResponse({"message": "No shows are availabe for this selection"})
