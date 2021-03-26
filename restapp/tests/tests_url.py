from django.test import  TestCase
from django.shortcuts import  reverse

class HomePageTests(TestCase):

    def test_home_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

    def test_home_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
