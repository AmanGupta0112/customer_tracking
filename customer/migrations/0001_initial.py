# Generated by Django 4.2.3 on 2023-07-30 15:13

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
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=15, null=True),
                ),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("linked_id", models.IntegerField(blank=True, null=True)),
                (
                    "link_precedence",
                    models.CharField(
                        choices=[("primary", "Primary"), ("secondary", "Secondary")],
                        default="primary",
                        max_length=10,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("deleted_at", models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
