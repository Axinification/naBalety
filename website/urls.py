from django.urls import path

from . import views

app_name = 'website'

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('wydarzenia/', views.events_page, name='events_page'),
    path('<slug:slug>/', views.event_details, name='event_details'),
]