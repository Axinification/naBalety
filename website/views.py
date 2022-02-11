from django.shortcuts import get_object_or_404, render

from .models import City, Club, Event, Ticket

#Main page
def main_page(request):
    events = Event.objects.all()
    return render(request, 'home.html', {'events': events})

#All events page
def events_page(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})

#Show events by city #TODO test if working
def events_by_city(request, city):
    events = get_object_or_404(Event, slug=city)
    return render(request, 'events.html', {'events': events})

#Show specific event
def event_details(request, slug):
    event = get_object_or_404(Event, slug=slug, visible=True)
    return render(request, 'event.html', {'event':event})

#Show ticket #TODO change to sometihin like Ticket.object.filter(user==user)
def ticket_details_by_id(request, id):
    ticket = get_object_or_404(Ticket, id=id)
    if ticket.bought_by: #TODO Add bought_by == user
        return render(request, 'ticket.html', {'ticket':ticket})
    else:
        return render(request, '404.html')

def clubs_by_city(request, city_slug):
    city = get_object_or_404(City, slug=city_slug)
    club = Club.objects.filter(city=city)
    return render(request, 'city.html')

# def events(request):
#     return {
#         'events': Event.objects.all()
#     }