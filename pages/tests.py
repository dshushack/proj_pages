from django.test import SimpleTestCase

class SimpleTests(SimpleTestCase):

    # test to ensure the home page successfully renders
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # test to ensure the about page successfully renders
    def test_about_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)