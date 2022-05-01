from django.contrib import admin

# Register your models here.
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    pass
admin.site.register(Movie, MovieAdmin)