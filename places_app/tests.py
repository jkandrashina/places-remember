from datetime import date

from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from .models import PlaceRemember


class PlaceModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='jay')
        self.place = PlaceRemember.objects.create(author=self.user, place_name='Стокгольм', comment='Комментарий о Стокгольме')

    def test_place_is_created(self):
        self.assertEqual(self.place.author, self.user)
        self.assertEqual(self.place.place_name, 'Стокгольм')
        self.assertEqual(self.place.comment, 'Комментарий о Стокгольме')
        self.assertEqual(self.place.pub_date, date.today())


class PlaceCreateTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='jay')
        self.auth_client = Client()
        self.auth_client.force_login(self.user)

    def test_user_can_add_new_place(self):
        self.auth_client.post(
            '/add-place/',
            {'place_name': 'Амстердам', 'comment': 'Комментарий об Амстердаме'}
        )
        places_list = PlaceRemember.objects.filter(id=1)
        self.assertEqual(places_list[0].place_name, 'Амстердам')
        self.assertEqual(places_list[0].comment, 'Комментарий об Амстердаме')


class PlacesListTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='jay')
        self.auth_client = Client()
        self.auth_client.force_login(self.user)
        PlaceRemember.objects.bulk_create([
            PlaceRemember(author=self.user, place_name='Париж', comment='Комментарий о Париже'),
            PlaceRemember(author=self.user, place_name='Лондон', comment='Комментарий о Лондоне')
        ])

    def test_status_code_is_200(self):
        response = self.auth_client.get(reverse('my_places'))
        self.assertEqual(response.status_code, 200)

    def test_template_is_correct(self):
        response = self.auth_client.get(reverse('my_places'))
        self.assertTemplateUsed(response, 'places_app/my-places.html')

    def test_context_is_correct(self):
        response = self.auth_client.get(reverse('my_places'))
        places_list = response.context['places']
        db_list = PlaceRemember.objects.all()
        self.assertEqual(places_list.count(), 2)
        self.assertQuerysetEqual(places_list, db_list, ordered=False)
