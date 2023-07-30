from django.urls import path,include
from .views import create_contact
app_name = 'customer'

urlpatterns = [
    path("create",create_contact,name="create"),

]