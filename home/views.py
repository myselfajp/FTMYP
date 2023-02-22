from django.shortcuts import render
from django.http import HttpResponse
from service.models import Expert
from .models import Contact
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def http_index(request):
    return render(request,"index.html")
    
def http_about(request):
    expert = Expert.objects.all()
    return render(request,"about.html",{"expert":expert})
    
@csrf_exempt
def http_contact(request):
    if request.method == "POST":
        try:
            contact=Contact()
            contact.name = request.POST.get("name")
            contact.email = request.POST.get("email")
            contact.message = request.POST.get("message")
            contact.save()
            return HttpResponse("success")
        except:
            return HttpResponse("unsuccess")
    return render(request,"contact.html")