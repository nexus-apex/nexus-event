from django.contrib import admin
from .models import Event, Attendee, Venue

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ["title", "event_type", "venue", "date", "capacity", "created_at"]
    list_filter = ["event_type", "status"]
    search_fields = ["title", "venue"]

@admin.register(Attendee)
class AttendeeAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "event_title", "ticket_type", "created_at"]
    list_filter = ["ticket_type", "status"]
    search_fields = ["name", "email", "phone"]

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ["name", "capacity", "hourly_rate", "contact", "status", "created_at"]
    list_filter = ["status"]
    search_fields = ["name", "contact", "phone"]
