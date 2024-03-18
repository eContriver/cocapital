# Generated by Django 5.0.3 on 2024-03-13 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ContactSubmission",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("message", models.TextField()),
                ("ip_address", models.GenericIPAddressField()),
                ("submission_time", models.DateTimeField(auto_now_add=True)),
                ("resolved", models.BooleanField(default=False)),
            ],
        ),
    ]