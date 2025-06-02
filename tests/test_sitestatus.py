# tests/test_sitestatus.py
from django.test import TestCase
from rest_framework.test import APIClient
from ravipangali_sites_status_attacker.models import SiteStatus

class SiteStatusTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_site_status(self):
        response = self.client.post(
            '/change-site-status/',
            {'status': True, 'description': 'Site is up'},
            format='json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['message'], 'Site status changed successfully')
        site_status = SiteStatus.objects.first()
        self.assertTrue(site_status.status)
        self.assertEqual(site_status.description, 'Site is up')