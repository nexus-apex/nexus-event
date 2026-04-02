from django.urls import path
from . import views

urlpatterns = [
    path('', lambda r: views.redirect('/dashboard/')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('events/', views.event_list, name='event_list'),
    path('events/create/', views.event_create, name='event_create'),
    path('events/<int:pk>/edit/', views.event_edit, name='event_edit'),
    path('events/<int:pk>/delete/', views.event_delete, name='event_delete'),
    path('attendees/', views.attendee_list, name='attendee_list'),
    path('attendees/create/', views.attendee_create, name='attendee_create'),
    path('attendees/<int:pk>/edit/', views.attendee_edit, name='attendee_edit'),
    path('attendees/<int:pk>/delete/', views.attendee_delete, name='attendee_delete'),
    path('venues/', views.venue_list, name='venue_list'),
    path('venues/create/', views.venue_create, name='venue_create'),
    path('venues/<int:pk>/edit/', views.venue_edit, name='venue_edit'),
    path('venues/<int:pk>/delete/', views.venue_delete, name='venue_delete'),
    path('settings/', views.settings_view, name='settings'),
    path('api/stats/', views.api_stats, name='api_stats'),
]
