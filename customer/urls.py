from django.urls import path,include
from .views import create_contact,identify_contact
app_name = 'customer'

urlpatterns = [
    path("create/",create_contact,name="create"),
    path('identify/', identify_contact, name='identify'),
]