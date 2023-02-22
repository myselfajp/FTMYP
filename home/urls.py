from django.urls import path
from .views import http_index,http_about,http_contact

app_name="home"

urlpatterns = [
    path("",http_index,name='index'),
    path("about",http_about,name='about'),
    path("contact",http_contact,name='contact'),
]

