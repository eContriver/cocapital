"""
Copyright (c) 2024 Perpetuator LLC

This file is part of Capital Copilot by Perpetuator LLC and is released under the MIT License.
See the LICENSE file in the root of this project for the full license text.
"""

from django.contrib import admin

from .models import ContactSubmission, UserPreferences

admin.site.register(ContactSubmission)
admin.site.register(UserPreferences)
