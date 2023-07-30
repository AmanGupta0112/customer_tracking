from django.shortcuts import render
from .models import Contact
from .serializers import ContactSerializer

# Create your views here.



def create_contact(request):
    data = request.POST.get()
    pass