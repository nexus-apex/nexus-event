from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Event, Attendee, Venue
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Seed NexusEvent with demo data'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@nexusevent.com', 'Admin@2024')
            self.stdout.write(self.style.SUCCESS('Admin user created'))

        if Event.objects.count() == 0:
            for i in range(10):
                Event.objects.create(
                    title=f"Sample Event {i+1}",
                    event_type=random.choice(["conference", "workshop", "seminar", "webinar", "social"]),
                    venue=f"Sample {i+1}",
                    date=date.today() - timedelta(days=random.randint(0, 90)),
                    capacity=random.randint(1, 100),
                    registered=random.randint(1, 100),
                    price=round(random.uniform(1000, 50000), 2),
                    status=random.choice(["upcoming", "live", "completed", "cancelled"]),
                    description=f"Sample description for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 Event records created'))

        if Attendee.objects.count() == 0:
            for i in range(10):
                Attendee.objects.create(
                    name=["Rajesh Kumar","Priya Sharma","Amit Patel","Deepa Nair","Vikram Singh","Ananya Reddy","Suresh Iyer","Meera Joshi","Karthik Rao","Fatima Khan"][i],
                    email=f"demo{i+1}@example.com",
                    phone=f"+91-98765{43210+i}",
                    event_title=["Rajesh Kumar","Priya Sharma","Amit Patel","Deepa Nair","Vikram Singh","Ananya Reddy","Suresh Iyer","Meera Joshi","Karthik Rao","Fatima Khan"][i],
                    ticket_type=random.choice(["general", "vip", "speaker", "sponsor"]),
                    status=random.choice(["registered", "confirmed", "checked_in", "cancelled"]),
                    amount_paid=round(random.uniform(1000, 50000), 2),
                )
            self.stdout.write(self.style.SUCCESS('10 Attendee records created'))

        if Venue.objects.count() == 0:
            for i in range(10):
                Venue.objects.create(
                    name=f"Sample Venue {i+1}",
                    address=f"Sample address for record {i+1}",
                    capacity=random.randint(1, 100),
                    hourly_rate=round(random.uniform(1000, 50000), 2),
                    amenities=f"Sample amenities for record {i+1}",
                    contact=f"Sample {i+1}",
                    status=random.choice(["available", "booked", "maintenance"]),
                    phone=f"+91-98765{43210+i}",
                )
            self.stdout.write(self.style.SUCCESS('10 Venue records created'))
