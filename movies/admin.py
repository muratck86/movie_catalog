from django.contrib import admin
from .models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "year", "duration", "created_date", "isReleased")
    list_display_links = ("id", "name", "year", "duration", "created_date")
    list_filter = ("year", "created_date")
    search_fields = ("name", "description")
    list_editable = ("isReleased",)
    list_per_page = 20


# Register your models here.
admin.site.register(Movie, MovieAdmin)