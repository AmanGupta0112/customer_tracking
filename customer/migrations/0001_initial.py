# Generated by Django 4.2.3 on 2023-07-30 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("phoneNumber", models.CharField(blank=True, max_length=15, null=True)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("linkedId", models.IntegerField(blank=True, null=True)),
                (
                    "linkPrecedence",
                    models.CharField(
                        choices=[("primary", "Primary"), ("secondary", "Secondary")],
                        default="primary",
                        max_length=10,
                    ),
                ),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                ("updatedAt", models.DateTimeField(auto_now=True)),
                ("deletedAt", models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
