from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    path("dj-rest-auth/registration/", include("dj_rest_auth.registration.urls")),
    path("admin/", admin.site.urls),
    path("", include("api.urls")),
]
