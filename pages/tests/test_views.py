from django.test import TestCase, Client
from django.urls import reverse
from courses.models import *
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.pricing_url = reverse("pricing")
        self.features_url = reverse("features")
        self.download_url = reverse("download")
        self.lifestyle_url = reverse("lifestyle")
        self.programs_url = reverse("programs")

    def test_pricing_GET(self):
        response = self.client.get(self.pricing_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pricing.html")

    def test_pricing_GET(self):
        response = self.client.get(self.features_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "features.html")

    def test_download_GET(self):
        response = self.client.get(self.download_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "download.html")

    def test_lifestyle_GET(self):
        response = self.client.get(self.lifestyle_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lifestyle.html")

    def test_programs_GET(self):
        response = self.client.get(self.programs_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "programs.html")
