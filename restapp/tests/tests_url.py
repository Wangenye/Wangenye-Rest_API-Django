from django.test import  TestCase
from django.shortcuts import  reverse

class AllPagesTests(TestCase):

    def test_home_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)
        

    def test_home_url_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'restapp/items.html')

    def test_signup_status(self):
        response = self.client.get('/signup')
        self.assertEqual(response.status_code,200)
        
    def test_signup_url_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'customerApp/signup.html')


    def test_customerapi_status(self):
        response = self.client.get('/customerapi/')
        self.assertEqual(response.status_code,200)
        
    def test_signup_url_name(self):
        response = self.client.get(reverse('customer_api'))
        self.assertEqual(response.status_code,200)
        # self.assertTemplateUsed(response,'customerApp/signup.html')
