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
        self.url = '/api/deposits/'

    def test_deposit_creation(self):
        data = {
            'amount': 100.0,
            'currency': 'USDT',
            'trx_id': 'test123'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # serializer returns decimals as strings
        self.assertEqual(response.data['amount'], '100.00')
        self.assertEqual(response.data['currency'], 'USDT')
        self.assertEqual(response.data['status'], 'pending')

    def test_missing_amount(self):
        data = {
            'currency': 'USDT',
            'trx_id': 'test123'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('amount', response.data)

    def test_invalid_amount(self):
        data = {
            'amount': -100.0,
            'currency': 'USDT',
            'trx_id': 'test123'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('amount', response.data)

    def test_invalid_currency(self):
        data = {
            'amount': 10.0,
            'currency': 'DOGE',
            'trx_id': 'test999'
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('currency', response.data)

    def test_long_trx_id(self):
        data = {
            'amount': 100.0,
            'currency': 'USDT',
            'trx_id': 'x' * 100,  # 100‑char trx_id
            'status': 'pending'
        }
        response = self.client.post('/api/deposits/', data, format='json')
        # now expecting CREATED since max_length on trx_id permits 100 chars
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['trx_id'], 'x' * 100)

    def test_list_pagination(self):
        # create 15 deposits directly
        for i in range(15):
            Deposit.objects.create(
                user=self.user,
                amount=1 + i,
                currency='BTC',
                trx_id=f'pagetest{i}'
            )
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # pagination envelope keys
        self.assertIn('count', response.data)
        self.assertIn('results', response.data)
        self.assertEqual(response.data['count'], 15)
        # default PAGE_SIZE = 10, so results length should be 10
        self.assertEqual(len(response.data['results']), 10)

    def test_unauthorized_access(self):
        unauthenticated_client = APIClient()
        response = unauthenticated_client.get('/api/deposits/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_duplicate_trx_id(self):
        Deposit.objects.create(
            user=self.user,
            amount=100,
            currency='USDT',
            trx_id='duplicate123'
        )
        data = {
            'amount': 200,
            'currency': 'USDT',
            'trx_id': 'duplicate123',
            'status': 'pending'
        }
        response = self.client.post('/api/deposits/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('trx_id', response.data)

