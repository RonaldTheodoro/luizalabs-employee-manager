from django.test import TestCase
from django.urls import reverse


class IndexViewTest(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('core:index'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'index.html')
