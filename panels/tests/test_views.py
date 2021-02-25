from django.test import SimpleTestCase



class TestIndex(SimpleTestCase):

    def test_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

