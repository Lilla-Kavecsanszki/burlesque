from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "subscription", "subscribed_at")
    list_filter = ("subscription", "subscribed_at")
    search_fields = ("user__username", "user__email")
    ordering = ("-subscribed_at",)
