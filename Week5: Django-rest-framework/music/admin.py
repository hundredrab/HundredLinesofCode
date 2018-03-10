from django.contrib import admin
from .models import Artist, Track
# Register your models here.

admin.site.register(Track)
admin.site.register(Artist)