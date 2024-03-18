# Generated by Django 5.0.3 on 2024-03-17 22:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


def set_default_user(apps, schema_editor):
    User = apps.get_model(settings.AUTH_USER_MODEL)
    user = User.objects.order_by("id").first()  # Gets the first user
    if not user:
        user = User.objects.create(username="default_user")  # Creates a new user if none exists
    UserPreferences = apps.get_model("users", "UserPreferences")
    for pref in UserPreferences.objects.all():
        pref.user = user
        pref.save()


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_userpreferences"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="userpreferences",
            name="user",
            field=models.OneToOneField(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="preferences",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.RunPython(set_default_user, reverse_code=migrations.RunPython.noop),
    ]
