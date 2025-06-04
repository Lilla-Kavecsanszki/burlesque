from django.contrib import admin
from .models import Show

class ShowAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "city",
        "address",
        "date",
        "show_type",
        "price",
    )
    list_filter = ("featured_on_homepage", "city", "show_type", "date")
    search_fields = ("title", "address", "description", "city")
    ordering = ("-date",)

admin.site.register(Show, ShowAdmin)