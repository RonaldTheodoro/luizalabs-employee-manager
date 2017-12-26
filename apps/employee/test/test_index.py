from django.test import TestCase
from django.urls import reverse, resolve

from .. import views


class IndexViewTest(TestCase):

    def setUp(self):
        self.response = self.client.get(reverse('index'))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'index.html')

    def test_index_view_function(self):
        view = resolve(reverse('index'))
        self.assertEqual(view.func, views.index)
