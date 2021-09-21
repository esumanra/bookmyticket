from django.test import TestCase
from django.contrib.auth.models import User
from .models import *


class LoginTest(TestCase):
    def setUp(self):
        self.credentials = {"username": "testuser", "password": "secret"}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        response = self.client.post(
            "/dj-rest-auth/login/", self.credentials, follow=True
        )
        self.assertTrue(response.json().get("key", False))

    def test_invalid_login(self):
        credentials = {"username": "testuser2", "password": "secret"}
        response = self.client.post("/dj-rest-auth/login/", credentials, follow=True)
        self.assertFalse(response.json().get("key", False))


class BookingTest(TestCase):
    def setUp(self):
        # Adding a test user
        self.credentials = {"username": "testuser", "password": "secret"}
        self.user = User.objects.create_user(**self.credentials)

        # adding movie and show details
        Movie.objects.create(name="Uppena", language="Telugu")
        movie = Movie.objects.get(name__iexact="Uppena")
        City.objects.create(name="Hyderabad")
        city = City.objects.get(name__iexact="Hyderabad")
        Theatre.objects.create(name="AMB", city_id=city.id)
        theatre = Theatre.objects.get(name__iexact="AMB")
        Show.objects.create(
            name="Morning",
            start_time="2020-09-29 10:00",
            end_time="2020-09-29 12:30",
        )
        show = Show.objects.get(id=1)
        Mapping.objects.create(movie=movie, theatre=theatre, show=show, city=city)

    def get_token(self, credentials):
        response = self.client.post("/dj-rest-auth/login/", credentials, follow=True)
        token = response.json().get("key", None)
        return token

    def test_book_ticket_valid_user(self):
        token = self.get_token(self.credentials)
        body = {
            "city_name": "hyderabad",
            "movie_name": "Uppena",
            "theatre_name": "AMB",
            "show_name": "Morning",
            "ticket_nos": "1",
        }
        headers = {"HTTP_AUTHORIZATION": f"Token {token}"}
        response = self.client.post("/book", **body, **headers)
        self.assertTrue = response.status_code == 200

    def test_book_ticket_invalid_user(self):
        body = {
            "city_name": "hyderabad",
            "movie_name": "Uppena",
            "theatre_name": "AMB",
            "show_name": "Morning",
            "ticket_nos": "1",
        }
        response = self.client.post("/book", **body)
        self.assertTrue = response.status_code != 200
