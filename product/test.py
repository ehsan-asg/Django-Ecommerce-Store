from django.test import TestCase
from .models import Category, Feature, Discount, Brand, Product

class ModelTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category")
        self.feature = Feature.objects.create(name="Test Feature", price=100)
        self.discount = Discount.objects.create(title="Test Discount", type="percent", amount=10, min_amount=50, max_amount=100, active=True)
        self.brand = Brand.objects.create(name="Test Brand")
        self.product = Product.objects.create(name="Test Product", brand=self.brand, description="Test Description", feature_basic="Test Feature Basic", discount=self.discount)

    def test_category_creation(self):
        category = Category.objects.get(name="Test Category")
        self.assertEqual(category.name, "Test Category")

    def test_feature_creation(self):
        feature = Feature.objects.get(name="Test Feature")
        self.assertEqual(feature.name, "Test Feature")
        self.assertEqual(feature.price, 100)

    def test_discount_creation(self):
        discount = Discount.objects.get(title="Test Discount")
        self.assertEqual(discount.title, "Test Discount")
        self.assertEqual(discount.type, "percent")
        self.assertEqual(discount.amount, 10)
        self.assertEqual(discount.min_amount, 50)
        self.assertEqual(discount.max_amount, 100)
        self.assertTrue(discount.active)

    def test_brand_creation(self):
        brand = Brand.objects.get(name="Test Brand")
        self.assertEqual(brand.name, "Test Brand")

    def test_product_creation(self):
        product = Product.objects.get(name="Test Product")
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.brand, self.brand)
        self.assertEqual(product.description, "Test Description")
        self.assertEqual(product.feature_basic, "Test Feature Basic")
        self.assertEqual(product.discount, self.discount)
