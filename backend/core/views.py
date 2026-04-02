import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum, Count
from .models import Event, Attendee, Venue


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        error = 'Invalid credentials. Try admin / Admin@2024'
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def dashboard_view(request):
    ctx = {}
    ctx['event_count'] = Event.objects.count()
    ctx['event_conference'] = Event.objects.filter(event_type='conference').count()
    ctx['event_workshop'] = Event.objects.filter(event_type='workshop').count()
    ctx['event_seminar'] = Event.objects.filter(event_type='seminar').count()
    ctx['event_total_price'] = Event.objects.aggregate(t=Sum('price'))['t'] or 0
    ctx['attendee_count'] = Attendee.objects.count()
    ctx['attendee_general'] = Attendee.objects.filter(ticket_type='general').count()
    ctx['attendee_vip'] = Attendee.objects.filter(ticket_type='vip').count()
    ctx['attendee_speaker'] = Attendee.objects.filter(ticket_type='speaker').count()
    ctx['attendee_total_amount_paid'] = Attendee.objects.aggregate(t=Sum('amount_paid'))['t'] or 0
    ctx['venue_count'] = Venue.objects.count()
    ctx['venue_available'] = Venue.objects.filter(status='available').count()
    ctx['venue_booked'] = Venue.objects.filter(status='booked').count()
    ctx['venue_maintenance'] = Venue.objects.filter(status='maintenance').count()
    ctx['venue_total_hourly_rate'] = Venue.objects.aggregate(t=Sum('hourly_rate'))['t'] or 0
    ctx['recent'] = Event.objects.all()[:10]
    return render(request, 'dashboard.html', ctx)


@login_required
def event_list(request):
    qs = Event.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(title__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(event_type=status_filter)
    return render(request, 'event_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def event_create(request):
    if request.method == 'POST':
        obj = Event()
        obj.title = request.POST.get('title', '')
        obj.event_type = request.POST.get('event_type', '')
        obj.venue = request.POST.get('venue', '')
        obj.date = request.POST.get('date') or None
        obj.capacity = request.POST.get('capacity') or 0
        obj.registered = request.POST.get('registered') or 0
        obj.price = request.POST.get('price') or 0
        obj.status = request.POST.get('status', '')
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/events/')
    return render(request, 'event_form.html', {'editing': False})


@login_required
def event_edit(request, pk):
    obj = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        obj.title = request.POST.get('title', '')
        obj.event_type = request.POST.get('event_type', '')
        obj.venue = request.POST.get('venue', '')
        obj.date = request.POST.get('date') or None
        obj.capacity = request.POST.get('capacity') or 0
        obj.registered = request.POST.get('registered') or 0
        obj.price = request.POST.get('price') or 0
        obj.status = request.POST.get('status', '')
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/events/')
    return render(request, 'event_form.html', {'record': obj, 'editing': True})


@login_required
def event_delete(request, pk):
    obj = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/events/')


@login_required
def attendee_list(request):
    qs = Attendee.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(ticket_type=status_filter)
    return render(request, 'attendee_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def attendee_create(request):
    if request.method == 'POST':
        obj = Attendee()
        obj.name = request.POST.get('name', '')
        obj.email = request.POST.get('email', '')
        obj.phone = request.POST.get('phone', '')
        obj.event_title = request.POST.get('event_title', '')
        obj.ticket_type = request.POST.get('ticket_type', '')
        obj.status = request.POST.get('status', '')
        obj.amount_paid = request.POST.get('amount_paid') or 0
        obj.save()
        return redirect('/attendees/')
    return render(request, 'attendee_form.html', {'editing': False})


@login_required
def attendee_edit(request, pk):
    obj = get_object_or_404(Attendee, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.email = request.POST.get('email', '')
        obj.phone = request.POST.get('phone', '')
        obj.event_title = request.POST.get('event_title', '')
        obj.ticket_type = request.POST.get('ticket_type', '')
        obj.status = request.POST.get('status', '')
        obj.amount_paid = request.POST.get('amount_paid') or 0
        obj.save()
        return redirect('/attendees/')
    return render(request, 'attendee_form.html', {'record': obj, 'editing': True})


@login_required
def attendee_delete(request, pk):
    obj = get_object_or_404(Attendee, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/attendees/')


@login_required
def venue_list(request):
    qs = Venue.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'venue_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def venue_create(request):
    if request.method == 'POST':
        obj = Venue()
        obj.name = request.POST.get('name', '')
        obj.address = request.POST.get('address', '')
        obj.capacity = request.POST.get('capacity') or 0
        obj.hourly_rate = request.POST.get('hourly_rate') or 0
        obj.amenities = request.POST.get('amenities', '')
        obj.contact = request.POST.get('contact', '')
        obj.status = request.POST.get('status', '')
        obj.phone = request.POST.get('phone', '')
        obj.save()
        return redirect('/venues/')
    return render(request, 'venue_form.html', {'editing': False})


@login_required
def venue_edit(request, pk):
    obj = get_object_or_404(Venue, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.address = request.POST.get('address', '')
        obj.capacity = request.POST.get('capacity') or 0
        obj.hourly_rate = request.POST.get('hourly_rate') or 0
        obj.amenities = request.POST.get('amenities', '')
        obj.contact = request.POST.get('contact', '')
        obj.status = request.POST.get('status', '')
        obj.phone = request.POST.get('phone', '')
        obj.save()
        return redirect('/venues/')
    return render(request, 'venue_form.html', {'record': obj, 'editing': True})


@login_required
def venue_delete(request, pk):
    obj = get_object_or_404(Venue, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/venues/')


@login_required
def settings_view(request):
    return render(request, 'settings.html')


@login_required
def api_stats(request):
    data = {}
    data['event_count'] = Event.objects.count()
    data['attendee_count'] = Attendee.objects.count()
    data['venue_count'] = Venue.objects.count()
    return JsonResponse(data)
