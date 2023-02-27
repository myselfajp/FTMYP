from django.shortcuts import render
from .models import Service,ServiceType,Reference
# from django.http import HttpResponse

# Create your views here.
def http_all_services(request):
    service_type = ServiceType.objects.all()
    services = Service.objects.all()
    context={
        "service_type":service_type,
        "services":services
    }
    return render(request,"services.html",context=context)

    
def http_single_services(request,s_id):
    service = Service.objects.get(id=s_id)
    context={
        "service":service
    }
    return render(request,"single_service.html",context=context)


def http_all_references(request):
    service_type = ServiceType.objects.all()
    references = Reference.objects.all().order_by("name")
    context={
        "service_type":service_type,
        "references":references
    }
    return render(request,"references.html",context=context)

def http_single_reference(request,r_id):
    reference = Reference.objects.get(id=r_id)
    context={
        "reference":reference
    }
    return render(request,"reference_single.html",context=context)