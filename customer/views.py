from django.shortcuts import render
from .models import Contact
from django.db.models import Q
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def create_contact(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get("email")
        phone_number = data.get("phone_number")
        # Search for an existing contact based on email or phone number
        contact = Contact.objects.filter(Q(email=email) | Q(phone_number=phone_number)).order_by("created_at").first()
        # Initialize link_precedence and linked_id variables
        link_precedence = "primary"
        linked_id = None
        try:
            if contact:
                link_precedence = "secondary"
                linked_id = contact.id
            else:  
                link_precedence = "primary"
        except Exception as e:
            print(f"Error Caused by {e}")
    
    obj = Contact.objects.create(email=email,
                                phone_number=phone_number, 
                                linked_id=linked_id, 
                                link_precedence=link_precedence)
    return JsonResponse({"detail": "Successfully Created !!","Contact_id":obj.id}, status=201)


@csrf_exempt
def identify_contact(request):

    # Assuming you have already set up the Contact model as described in the previous discussions
    if request.method == 'POST':
        # Get the JSON data from the request
        data = json.loads(request.body)
        email = data.get('email')
        phone_number = data.get('phone_number')
        if email or phone_number:
            # Query the database to find the customer's contact information
            try:
                if email:
                    primary_contact = Contact.objects.filter(email=email, link_precedence='primary').first()
                else:
                    primary_contact = Contact.objects.filter(phone_number=phone_number, link_precedence='primary').first()

                if primary_contact:
                    secondary_contacts = Contact.objects.filter(linked_id=primary_contact.id)
                    secondary_contact_ids = [contact.id for contact in secondary_contacts]

                    response_data = {
                        "contact": {
                            "primaryContactId": primary_contact.id,
                            "emails": [primary_contact.email] + [contact.email for contact in secondary_contacts],
                            "phone_numbers": [primary_contact.phone_number] + [contact.phone_number for contact in secondary_contacts],
                            "secondaryContactIds": secondary_contact_ids
                        }
                    }

                    return JsonResponse(response_data)
                else:
                    # If the primary contact is not found, return an appropriate response
                    return JsonResponse({"error": "No contact found for the provided email or phone number."}, status=404)
            except Exception as e:
                # Handle any potential exceptions or errors gracefully
                return JsonResponse({"error": "An error occurred while processing the request."}, status=500)
        else:
            # If neither email nor phone number is provided, return an appropriate response
            return JsonResponse({"error": "Please provide either email or phone number."}, status=400)
    else:
        # Only handle POST requests for this view
        return JsonResponse({"error": "Invalid request method. Only POST requests are allowed."}, status=405)
