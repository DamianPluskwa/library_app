from django.test import TestCase

# Create your tests here.
from django.urls import reverse


class TestViewsRentedList(TestCase):
    def test_(self):
        response = self.client.get(reverse('library:rented_list'))
        self.assertEqual(response.status_code, 200)

    def test_2(self):
        response = self.client.get(reverse('library:rented_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Powrót do listy dostępnych książek.')

    def test_3(self):
        response = self.client.get(reverse('library:rented_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Brak dostępnych książek')
        self.assertNotContains(response, 'Minęła data zwrotu.')

    def test_4(self):
        response = self.client.get(reverse('library:rented_list'))
        self.assertEqual(response.status_code, 200)

