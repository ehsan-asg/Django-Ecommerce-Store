import pytest
from django.test import TestCase
from django.utils import timezone
from .models import Category, Feature, Discount, Product


class TestCategoryModel(TestCase):

    def test_category_str_method(self):
        category = Category.objects.create(name='Test Category', slug='test-category')
        self.assertEqual(str(category), "Test Category")


class TestFeatureModel(TestCase):

    def test_feature_str_method(self):
        feature = Feature.objects.create(name='Test Feature', value=10, price=100)
        self.assertEqual(str(feature), "Test Feature")


class TestDiscountModel(TestCase):

    def test_discount_str_method(self):
        discount = Discount.objects.create(title='Test Discount', type='percent', amount=10, min_amount=100, max_amount=200, valid_from=timezone.now(), valid_to=timezone.now())
        self.assertEqual(str(discount), "Test Discount")


class TestProductModel(TestCase):

    def test_product_str_method(self):
        product = Product.objects.create(name='Test Product', slug='test-product', description='Test Description', feature_basic='Test Basic Feature', available=True)
        self.assertEqual(str(product), "Test Product")
