from django.db import models

class Category(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='scategory', null=True, blank=True)
    is_sub = models.BooleanField(default=False)
    name=models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self) -> str:
        return self.name

class Feature(models.Model):
     name = models.CharField(max_length=100)
     value = models.IntegerField()
     price = models.IntegerField()
     created = models.DateTimeField(auto_now_add=True)
     updated = models.DateTimeField(auto_now=True)
    
     def __str__(self):
        return self.name
    
     

class Discount(models.Model):
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
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title

class Product(models.Model):
    Category = models.ManyToManyField(Category,related_name="products")
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True)
    feature = models.ManyToManyField(Feature)
    image = models.ImageField(upload_to ='uploads/% Y/% m/% d/') 
    description = models.TextField()
    feature_basic = models.TextField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    discount = models.ForeignKey(Discount,on_delete=models.CASCADE,related_name="disproducts",null=True, blank=True)

    class Meta:
         ordering = ('-updated',)

    def __str__(self) -> str:
        return self.name
