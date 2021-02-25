from django.test import SimpleTestCase

from django.urls import reverse, resolve


class TestIndex(SimpleTestCase):

    def test_reverse(self):
        url = reverse('panels:home')
        self.assertEquals(url, '/')

    def test_resolve(self):
        url = resolve('/')
        self.assertEquals(url.namespace, 'panels')
        self.assertEquals(url.url_name, 'home')
        self.assertEquals(url.view_name, 'panels:home')
