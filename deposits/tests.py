from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework import status
from django.test import TestCase
from .models import Deposit

class DepositViewSetTest(TestCase):

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(email="testuser@example.com", password="password")
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_deposit_creation(self):
        # Test POST request to create a deposit
        data = {
            'amount': 100.0,
            'currency': 'USDT',
            'trx_id': 'test123',
            'status': 'pending'
        }
        response = self.client.post('/api/deposits/', data, format='json')

        # Check if the deposit is created and status code is 201 (Created)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['amount'], '100.00')  # Compare as a string
        self.assertEqual(response.data['currency'], 'USDT')
        self.assertEqual(response.data['status'], 'pending')

    def test_missing_amount(self):
        # Test POST request with missing 'amount' field
        data = {
            'currency': 'USDT',
            'trx_id': 'test123',
            'status': 'pending'
        }
        response = self.client.post('/api/deposits/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('amount', response.data)  # Ensure the error message contains 'amount'

    def test_invalid_amount(self):
        # Test POST request with an invalid negative 'amount'
        data = {
            'amount': -100.0,  # Invalid negative amount
            'currency': 'USDT',
            'trx_id': 'test123',
            'status': 'pending'
        }
        response = self.client.post('/api/deposits/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('amount', response.data)  # Ensure the error message contains 'amount'

    def test_large_amount(self):
        # Test POST request with a very large 'amount'
        data = {
            'amount': 1000000000.0,  # Extremely large amount
            'currency': 'USDT',
            'trx_id': 'test123',
            'status': 'pending'
        }
        response = self.client.post('/api/deposits/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['amount'], '1000000000.00')  # Check if large amount is saved

    def test_long_trx_id(self):
        # Test POST request with a very long 'trx_id'
        data = {
            'amount': 100.0,
            'currency': 'USDT',
            'trx_id': 'x' * 100,  # A 255-character long transaction ID
            'status': 'pending'
        }
        response = self.client.post('/api/deposits/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['trx_id'], 'x' * 100)  # Ensure the long trx_id is saved correctly
