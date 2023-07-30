from django.db import models

class Contact(models.Model):
    PRIMARY = "primary"
    SECONDARY = "secondary"

    LINK_PRECEDENCE_CHOICES = [
        (PRIMARY, "Primary"),
        (SECONDARY, "Secondary"),
    ]

    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    linked_id = models.IntegerField(blank=True, null=True)
    link_precedence = models.CharField(
        max_length=10, choices=LINK_PRECEDENCE_CHOICES, default=PRIMARY
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Contact (ID: {self.id}, Email: {self.email}, Phone: {self.phone_number})"
