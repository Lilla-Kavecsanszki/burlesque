from django.contrib import admin
from .models import Team, TeamImage, TeamVideo

class TeamImageInline(admin.TabularInline):
    model = TeamImage
    extra = 1  # Number of extra forms to display for adding images

class TeamVideoInline(admin.TabularInline):
    model = TeamVideo
    extra = 1


class TeamAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "date", "city", "show_type")
    search_fields = ("name", "description")
    ordering = ("name",)
    inlines = [TeamImageInline, TeamVideoInline]


admin.site.register(Team, TeamAdmin)
