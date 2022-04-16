from ..models import City, Club, Event
from django.test import TestCase


class TestEventsModel(TestCase):

    def setUp(self):
        self.city1 = City.objects.create(
            city="Gdynia", voivodeship="Pomorskie"
        )
        self.club1 = Club.objects.create(
            city_id=1, name="Club", address="Test 1"
        )
        self.event1 = Event.objects.create(
            name="Event", description="Description", club_id=1, visible=True,
            is_promotor=True, is_concert=False, price_1=30,
            pool_1=100, pool_date="18-04-2022 14:28:13", price_2=40,
            pool_2=200, event_date_time="20-04-2022 14:28:13"
        )

    def test_event_model_entry(self):
        event = self.event1
        self.assertTrue(isinstance(event, Event))
        self.assertEqual(str(event), "Event")
