from django.contrib import admin
from .models import Movie, WatchList, StreamPlatform, Review

# Register your models here.
admin.site.register(Movie)
admin.site.register(WatchList)
admin.site.register(StreamPlatform)
admin.site.register(Review)
