from django.db import models
from core.models import BaseModel
from colorfield.fields import ColorField
from django.utils.text import slugify
from galleryfield.fields import GalleryField
class Category(BaseModel):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)
    parent_categories = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='sub_categories')

    def __str__(self) -> str:
        return self.name
    


class Feature(BaseModel):
     name = models.CharField(max_length=100)
     value = ColorField(default='#FFFFFF')
     price = models.IntegerField()
    
     def __str__(self):
        return self.name
    
class Discount(BaseModel):
    discount_choise = (
    ('percent','percent'),
    ('amount', 'amount'),
    )
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=10,choices=discount_choise,default="percent")
    amount = models.IntegerField()
    min_amount = models.IntegerField()
    max_amount = models.IntegerField()
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

class Brand(BaseModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True,allow_unicode=True)
    image = models.ImageField(upload_to ='brands/%Y/%m/%d/',null=True,blank=True) 
    description = models.TextField(null=True,blank=True)
    def __str__(self):
        return self.name
class Product(BaseModel):
    Category = models.ManyToManyField(Category,related_name="products")
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True,allow_unicode=True)
    feature = models.ManyToManyField(Feature,related_name="pfeature")
    image = models.ImageField(upload_to ='products/%Y/%m/%d/',null=True,blank=True)
    brand =  models.ForeignKey(Brand,on_delete=models.CASCADE,related_name="pbrands")
    description = models.TextField()
    feature_basic = models.TextField()
    available = models.BooleanField(default=True)
    discount = models.ForeignKey(Discount,on_delete=models.CASCADE,related_name="disproducts",null=True, blank=True)

    class Meta:
         ordering = ('-created_at',)

    def __str__(self) -> str:
        return self.name
