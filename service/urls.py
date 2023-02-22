from django.urls import path
from .views import http_all_services,http_single_services,http_all_references,http_single_reference

app_name="service"

urlpatterns = [
    path("all_services",http_all_services,name='all_services'),
    path("service-<int:s_id>",http_single_services,name='single_service'),

    path("all_references",http_all_references,name='all_references'),
    path("reference-<int:r_id>",http_single_reference,name='single_reference'),
]

