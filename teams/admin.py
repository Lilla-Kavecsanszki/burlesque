from django.contrib import admin
from .models import Team

class TeamAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "date",
        "city",
        "show_type",
    )
    search_fields = ("name", "description")
    ordering = ("name",)

admin.site.register(Team, TeamAdmin)
