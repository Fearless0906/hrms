from django.contrib import admin
from .models import Goal, PerformanceCycle, Feedback, Review

# Register your models here.
admin.site.register(Goal)
admin.site.register(PerformanceCycle)
admin.site.register(Feedback)
admin.site.register(Review)
