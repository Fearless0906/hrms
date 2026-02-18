from django.contrib import admin
from .models import Announcement, PolicyDocument

# Register your models here.
admin.site.register(Announcement)
admin.site.register(PolicyDocument)