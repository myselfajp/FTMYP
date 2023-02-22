from django.contrib import admin
from .models import Service,Image,Reference,ServiceType,Expert

# Register your models here.
admin.site.register(Service)
admin.site.register(Image)
admin.site.register(Reference)
admin.site.register(ServiceType)
admin.site.register(Expert)

