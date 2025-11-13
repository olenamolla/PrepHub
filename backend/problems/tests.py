from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from django.urls import reverse
from django.utils import timezone
from problems.models import Problem


# Create your tests here.

# test class inheriting from APITestCase
# one test class per logical grouping
class ProblemAPITests(APITestCase):
    # special method that runs before each test methods
    # set up common state (like the URL) without repeating code
    def setUp(self):
        # DRF DefaultRouter names: <basename>-list. With queryset set,
        # basename is derived from the model name in lowercase: "problem".
        try:
            self.url = reverse('problem-list') # auto-generated name
        except Exception:
            # Fallback if reverse name does not resolve
            self.url = '/api/problems/'
    
    def test_list_returns_200_and_array(self):
        resp = self.client.get(self.url) # get request using DRF's test client
        self.assertEqual(resp.status_code, 200)
        self.assertIsInstance(resp.json(), list)
        
    def test_create_valid_returns_201_and_persists(self):
        payload = {
            "title": "Two Sum",
            "difficulty": "Easy",
            "topic": "Arrays",
            "notes": "First API created item",
            "solved_date": timezone.now().isoformat()
            
        }
        
        resp = self.client.post(self.url, payload, format ='json')
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(Problem.objects.count(), 1)
        self.assertEqual(resp.data.get('title'), "Two Sum")
        
    def test_create_invalid_returns_400(self):
        # Missing required fields like solved_date
        payload = {"title": "Invalid Payload"}
        resp = self.client.post(self.url, payload, format='json')
        self.assertEqual(resp.status_code, 400)
        self.assertIn('solved_date', resp.data)
 
    
