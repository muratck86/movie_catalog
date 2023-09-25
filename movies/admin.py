from django.contrib import admin
from .models import Movie, Person


class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "year", "duration", "created_date", "isReleased", "director")
    list_display_links = ("id", "name", "year", "duration", "created_date")
    list_filter = ("year", "created_date")
    search_fields = ("name", "description")
    list_editable = ("isReleased",)
    list_per_page = 20


class PersonAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "birth_date")
    list_display_links = list_display
    list_filter = ("birth_date",)
    search_fields = ("name",)
    list_per_page = 50

# Register your models here.
admin.site.register(Movie, MovieAdmin)
admin.site.register(Person, PersonAdmin)