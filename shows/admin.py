from django.contrib import admin
from .models import Show

class ShowAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "address",
        "dates",
    )
    list_filter = ("address",)
    search_fields = ("title", "address", "description")
    ordering = ("title",)

admin.site.register(Show, ShowAdmin)