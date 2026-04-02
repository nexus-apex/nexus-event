from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=255)
    event_type = models.CharField(max_length=50, choices=[("conference", "Conference"), ("workshop", "Workshop"), ("seminar", "Seminar"), ("webinar", "Webinar"), ("social", "Social")], default="conference")
    venue = models.CharField(max_length=255, blank=True, default="")
    date = models.DateField(null=True, blank=True)
    capacity = models.IntegerField(default=0)
    registered = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=50, choices=[("upcoming", "Upcoming"), ("live", "Live"), ("completed", "Completed"), ("cancelled", "Cancelled")], default="upcoming")
    description = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Attendee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, default="")
    phone = models.CharField(max_length=255, blank=True, default="")
    event_title = models.CharField(max_length=255, blank=True, default="")
    ticket_type = models.CharField(max_length=50, choices=[("general", "General"), ("vip", "VIP"), ("speaker", "Speaker"), ("sponsor", "Sponsor")], default="general")
    status = models.CharField(max_length=50, choices=[("registered", "Registered"), ("confirmed", "Confirmed"), ("checked_in", "Checked In"), ("cancelled", "Cancelled")], default="registered")
    amount_paid = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class Venue(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True, default="")
    capacity = models.IntegerField(default=0)
    hourly_rate = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    amenities = models.TextField(blank=True, default="")
    contact = models.CharField(max_length=255, blank=True, default="")
    status = models.CharField(max_length=50, choices=[("available", "Available"), ("booked", "Booked"), ("maintenance", "Maintenance")], default="available")
    phone = models.CharField(max_length=255, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
