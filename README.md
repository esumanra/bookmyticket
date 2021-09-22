# bookmyticket

### API Features
- Views movies playing in the city
- View shows for movies in the city
- Book a ticket for a show
- User registration, login/logout

### Project Tasks
- Only authenticated user can book a ticket
- Added logging
- CI pipeline
- CD pipeline with Azure

## API ENDPOINTS
```
[
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
  ```
### How to setup locally

#### Install dependencies
  ```
  > pip install -r requirements.txt
  ```
#### Run APP
  As sqlite3 db is already populated with data, just clone and run the app
  ```
  > python manange.py runserver
  ```
