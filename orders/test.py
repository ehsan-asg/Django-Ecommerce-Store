import pytest
from django.test import TestCase
from django.utils import timezone
from django.contrib.auth import get_user_model
from .models import Coupon, Order, OrderItem, Address
from product.models import Product

User = get_user_model()

class TestCouponModel(TestCase):

    def test_coupon_str_method(self):
        coupon = Coupon.objects.create(code="TEST123", valid_from=timezone.now(), valid_to=timezone.now(), discount=10)
        self.assertEqual(str(coupon), "TEST123")

class TestOrderModel(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_order_str_method(self):
        order = Order.objects.create(user=self.user)
        self.assertEqual(str(order), f'{self.user} - {str(order.id)}')

    def test_get_total_price_without_discount(self):
        product = Product.objects.create(name='Test Product')
        order = Order.objects.create(user=self.user)
        OrderItem.objects.create(order=order, product=product, price=100, quantity=2)
        self.assertEqual(order.get_total_price(), 200)

    def test_get_total_price_with_discount(self):
        product = Product.objects.create(name='Test Product')
        order = Order.objects.create(user=self.user, discount=10)
        OrderItem.objects.create(order=order, product=product, price=100, quantity=2)
        self.assertEqual(order.get_total_price(), 180)

class TestAddressModel(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_address_str_method(self):
        address = Address.objects.create(user=self.user, state='California', street='123 Test St', city='Test City', zip_code='12345', plate=10, unit=20)
        print(str(address))
        self.assertEqual(str(address), "123 Test St, Test City, California 12345")
