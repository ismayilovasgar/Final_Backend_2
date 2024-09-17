from django.test import SimpleTestCase
from django.urls import reverse, resolve
from courses.models import Course
from pages.views import *

# (
#     pricing,
#     features,
#     download,
#     lifestyle,
#     programs,
#     class01_detail_page,
#     class02_trainers,
#     blog_detail,
#     programs_detail,
# )


class TestUrls(SimpleTestCase):

    def test_pricing_url_resolves(self):
        url = reverse("pricing")
        self.assertEqual(resolve(url).func, pricing)

    def test_features_url_resolves(self):
        url = reverse("features")
        self.assertEqual(resolve(url).func, features)

    def test_download_url_resolves(self):
        url = reverse("download")
        self.assertEqual(resolve(url).func, download)

    def test_lifestyle_url_resolves(self):
        url = reverse("lifestyle")
        self.assertEqual(resolve(url).func, lifestyle)

    def test_programs_url_resolves(self):
        url = reverse("programs")
        self.assertEqual(resolve(url).func, programs)

    def test_class01_detail_url_resolves(self):
        url = reverse("class01_detail", args=[35])
        self.assertEqual(resolve(url).func, class01_detail_page)
        self.assertEqual(resolve(url).kwargs, {"id": 35})

    def test_class02_trainers_url_resolves(self):
        url = reverse("class02_trainers", args=["some-name"])
        self.assertEqual(resolve(url).func, class02_trainers)

    def test_blog_detail_url_resolves(self):
        url = reverse("blog_detail", args=[35])
        self.assertEqual(resolve(url).func, blog_detail)
        self.assertEqual(resolve(url).kwargs, {"id": 35})

    def test_programs_detail_url_resolves(self):
        url = reverse("programs_detail", args=[35])
        self.assertEqual(resolve(url).func, programs_detail)
        self.assertEqual(resolve(url).kwargs, {"id": 35})
