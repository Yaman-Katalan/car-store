from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Car

# Create your tests here.

class CarTests(TestCase):

    def test_list_page_status_code(self):
        url = reverse('car-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse('car-list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'cars/car_list.html')
        self.assertTemplateUsed(response, 'base.html')

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test_user',
            email='test@email.com',
            password='1234'
        )

        self.car = Car.objects.create(
            model='Civic',
            brand='Honda',
            price=20000.00,
            is_bought=True,
            buyer=self.user,
            buy_time='2023-05-15 10:00:00'
        )

    def test_str_method(self):
        self.assertEqual(str(self.car), "Civic (Honda)")

    def test_details_view(self):
        url = reverse('car-detail', args=[self.car.id])
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'cars/car_detail.html')

    def test_create_view(self):
        obj = {
            "model": "Model S",
            "brand": "Tesla",
            "price": 75000.00,
            "is_bought": False,
            "buyer": self.user.id,
            "buy_time": "2023-07-22 14:30:00"
        }

        url = reverse('car-create')
        response = self.client.post(path=url, data=obj, follow=True)
        self.assertRedirects(response, reverse('car-detail', args=[2]))
