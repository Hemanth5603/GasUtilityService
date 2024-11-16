from django.db import models
from django.contrib.auth.models import User



class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username

class ServiceRequest(models.Model):
    SERVICE_CHOICES = [
        ('Installation', 'Installation'),
        ('Repair', 'Repair'),
        ('Maintenance', 'Maintenance')
    ]

    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    description = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    status = models.CharField(max_length=50, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.request_type} - {self.customer.user.username}'


class SupportRepresentative(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    assigned_requests = models.ManyToManyField(ServiceRequest, blank=True)


    def __str__(self):
        return self.user.username