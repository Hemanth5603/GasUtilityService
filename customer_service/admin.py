from django.contrib import admin

from .models import CustomerProfile, ServiceRequest, SupportRepresentative

admin.site.register(CustomerProfile)
admin.site.register(ServiceRequest)
admin.site.register(SupportRepresentative)
