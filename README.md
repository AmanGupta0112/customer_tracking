# Customer Contact Identification

This web service provides an endpoint for identifying and tracking a customer's contact information across multiple purchases.

## Installation

1. Clone the repository to your local machine.
2. Install the required dependencies using `pip`:
   ```
   pip install -r requirements.txt
   ```
3. Run the Django development server:
   ```
   python manage.py runserver
   ```

## Endpoint
### `api/create/`
### `api/identify/`


**HTTP Method**: POST
**JSON Request Body Format For Create :**
```json
{
  "email": "string",
  "phoneNumber": "string"
}
```
**JSON Response Format For Create:**
```json
{
    "detail": "Successfully Created !!",
    "Contact_id": 15
}
```

**JSON Request Body Format For Identify:**
```json
{
  "email": "string",
  "phoneNumber": "string"
}
```


**JSON Response Format For Identify:**
```json
{
  "customerID": "string",
  "contact": {
    "primaryContactId": "number",
    "emails": ["string"],
    "phoneNumbers": ["string"],
    "secondaryContactIds": ["number"]
  }
}
```

## Usage

1. Send a POST request to the `api/identify/` endpoint with a JSON body containing either an email or a phone number, or both.
2. Send a POST request to the `api/create/` endpoint with a JSON body containing either an email or a phone number, or both.
3. The web service will return the customer's contact information, including the primary contact details and any associated secondary contacts.

## Requirements

- Python 3.x
- Django 3.x

## Contributing

We welcome contributions! If you find any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Feel free to customize the above template with more specific details about your project. The README.md file is essential for providing clear instructions on how to set up and use the web service, along with information about the API endpoint and response format.
