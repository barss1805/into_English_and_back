from django.contrib import admin

from .models import Sentence, Time, Success

admin.site.register("Sentence")
admin.site.register("Time")
admin.site.register("Success")