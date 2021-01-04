from django.contrib import admin
from .models import Therapist, TherapySession, AvailableTimeRange, TherapistSpecialties

# Register your models here.
admin.site.register(Therapist)
admin.site.register(TherapySession)
admin.site.register(AvailableTimeRange)
admin.site.register(TherapistSpecialties)
