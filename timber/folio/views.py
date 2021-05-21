from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
# Create your views here.



def index(request):
    return render(request, "index.html")

def cv(request):
    return render(request, "CV.html")
    pass

def contact(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        message = request.POST.get('message')

        contact.name = name
        contact.email = email
        contact.mobile = mobile
        contact.message = message
        contact.save()
        return HttpResponse("<h1>We Got Ur Mail</h1>")
        pass