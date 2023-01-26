from django.contrib import admin
from shortenurl_tracker.models import data, s_data
from .models import data,s_data
# Register your models here.
admin.site.register(data)
admin.site.register(s_data)
