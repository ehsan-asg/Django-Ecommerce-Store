from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from product.models import Product,Feature
from core.models import BaseModel

class Coupon(BaseModel):
	code = models.CharField(max_length=30, unique=True)
	valid_from = models.DateTimeField()
	valid_to = models.DateTimeField()
	discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(90)])
	active = models.BooleanField(default=False)

	def __str__(self):
		return self.code

class Order(BaseModel):
	user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='orders')
	is_paid = models.BooleanField(default=False)
	discount = models.IntegerField(blank=True, null=True, default=None)

	class Meta:
		ordering = ('-updated_at',)

	def __str__(self):
		return f'{self.user} - {str(self.id)}'

	def get_total_price(self):
		total = sum(item.get_cost() for item in self.items.all())
		if self.discount:
			discount_price = (self.discount / 100) * total
			return int(total - discount_price)
		return total
class OrderItem(BaseModel):
	order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	Feature = models.ForeignKey(Feature,on_delete=models.CASCADE,null=True,blank=True)
	price = models.IntegerField()
	quantity = models.IntegerField(default=1)

	def __str__(self):
		return str(self.id)

	def get_cost(self):
		return self.price * self.quantity

class Address(BaseModel):
     user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='uaddress')
     state = models.CharField(max_length=100)
     street = models.CharField(max_length=255)
     city = models.CharField(max_length=100)
     zip_code = models.CharField(max_length=20)
     plate = models.IntegerField()
     unit = models.IntegerField()
     
     def __str__(self):
        return f"{self.street}, {self.city}, {self.state} {self.zip_code}"
