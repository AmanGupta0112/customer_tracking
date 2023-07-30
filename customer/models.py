from django.db import models

class Contact(models.Model):
    PRIMARY = "primary"
    SECONDARY = "secondary"

    LINK_PRECEDENCE_CHOICES = [
        (PRIMARY, "Primary"),
        (SECONDARY, "Secondary"),
    ]

    phoneNumber = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    linkedId = models.IntegerField(blank=True, null=True)
    linkPrecedence = models.CharField(
        max_length=10, choices=LINK_PRECEDENCE_CHOICES, default=PRIMARY
    )
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    deletedAt = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Contact (ID: {self.id}, Email: {self.email}, Phone: {self.phoneNumber})"
