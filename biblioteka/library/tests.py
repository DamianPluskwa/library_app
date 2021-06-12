from django.test import TestCase

# Create your tests here.
from django.urls import reverse


class TestViewsRentedList(TestCase):
    def test(self):
        response = self.client.get(reverse('library:rented_list'))
        self.assertEqual(response.status_code, 200)

    #def test_2(self):
