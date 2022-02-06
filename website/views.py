from django.shortcuts import get_object_or_404, render

from .models import Event, Ticket

def main_page(request):
    events = Event.objects.all()
    return render(request, 'home.html', {'events': events})

def events_page(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})

def events_by_city(request, city):
    events = get_object_or_404(Event, city=city)
    return render(request, 'events.html', {'events': events})

def event_details(request, slug):
    event = get_object_or_404(Event, slug=slug, visible=True)
    return render(request, 'event.html', {'event':event})

def ticket_details_by_id(request, id):
    ticket = get_object_or_404(Ticket, id=id)
    if ticket.bought_by:
        return render(request, 'ticket.html', {'ticket':ticket})
    else:
        return render(request, '404.html')

# def events(request):
#     return {
#         'events': Event.objects.all()
#     }