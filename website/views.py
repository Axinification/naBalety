from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from django.db.models import Count

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
    pools = [event.pool_1, event.pool_2, event.pool_3, event.pool_4, event.pool_5, event.pool_6]
    pools_sum = sum(filter(None, pools))
    pools_number = len([x for x in pools if x != None])
    return date_checker(request, event, pools_number)

#Logic for deciding which pool is active
def date_checker(request, event, pools_number): 
    if timezone.now() < event.event_date_time: #TODO Czy dodać 10 minut przed zamknięciem zamykania puli?
        if  event.pool_date_5 and timezone.now() >= event.pool_date_5 or event.pool_5 and event.pool_5 <= event.ticket.filter(event=event ,pool_number=5).count():
            return render(request, 'event_details/event_6_pool.html', {'event':event, 'pools_number':pools_number})
        elif event.pool_date_4 and timezone.now() >= event.pool_date_4 or event.pool_4 and event.pool_4 <= event.ticket.filter(event=event ,pool_number=4).count():
            return render(request, 'event_details/event_5_pool.html', {'event':event, 'pools_number':pools_number})
        elif event.pool_date_3 and timezone.now() >= event.pool_date_3 or event.pool_3 and event.pool_3 <= event.ticket.filter(event=event ,pool_number=3).count():
            return render(request, 'event_details/event_4_pool.html', {'event':event, 'pools_number':pools_number})
        elif event.pool_date_2 and timezone.now() >= event.pool_date_2 or event.pool_2 and event.pool_2 <= event.ticket.filter(event=event ,pool_number=2).count():
            return render(request, 'event_details/event_3_pool.html', {'event':event, 'pools_number':pools_number})
        elif event.pool_date_1 and timezone.now() >= event.pool_date_1 or event.pool_1 and event.pool_1 <= event.ticket.filter(event=event ,pool_number=1).count():
            return render(request, 'event_details/event_2_pool.html', {'event':event, 'pools_number':pools_number})
        else:
            return render(request, 'event_details/event_1_pool.html', {'event':event, 'pools_number':pools_number})
    else:
        return render(request, 'event_details/event_ended.html', {'event':event})


#Show ticket #TODO change to sometihin like Ticket.object.filter(user==user)
def ticket_details_by_id(request, ticket_id):
    ticket = get_object_or_404(Ticket, ticket_id=ticket_id)
    if ticket.bought_by: #TODO Add bought_by == user
        return render(request, 'ticket.html', {'ticket':ticket})
    else:
        return render(request, '404.html')

#
def clubs_by_city(request, city_slug):
    city = get_object_or_404(City, slug=city_slug)
    club = Club.objects.filter(city=city)
    return render(request, 'city.html', {'city':city, 'club':club})
