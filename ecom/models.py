from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/CustomerProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name


class Product(models.Model):
    
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unisex')
    )

    SIZE = (
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Extra Extra Large')
    )

    SleeveLength = (
        ('SHORT', 'Short'),
        ('LONG', 'Long'),
        ('EXTRA_LONG', 'Extra Long'),
    )
    NeckType = (
        ('CREW', 'Crew'),
        ('V_NECK', 'V-Neck'),
        ('SCOOP', 'Scoop'),
    )

    Pattern = (
        ('SOLID', 'Solid'),
        ('STRIPED', 'Striped'),
        ('FLORAL', 'Floral'),
        ('GRAPHIC', 'Graphic'),
    )

    Occasion = (
        ('CASUAL', 'Casual'),
        ('FORMAL', 'Formal'),
        ('ACTIVE', 'Active'),

    )

    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_image/', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    gender = models.CharField(max_length=1, choices=GENDER)
    size = models.CharField(max_length=3, choices=SIZE)
    material = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    sleeve_length = models.CharField(max_length=255, choices=SleeveLength, blank=True)
    neck_type = models.CharField(max_length=255, choices=NeckType, blank=True)
    pattern = models.CharField(max_length=255, choices=Pattern, blank=True)
    occasion = models.CharField(max_length=255, choices=Occasion, blank=True)
    brand = models.CharField(max_length=255, default='Pinac')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], blank=True, null=True)
    stock_quantity = models.IntegerField(default=0)
    is_best_seller = models.BooleanField(default=False)
    is_new_arrival = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Orders(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Order Confirmed','Order Confirmed'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    )
    customer=models.ForeignKey('Customer', on_delete=models.CASCADE,null=True)
    product=models.ForeignKey('Product',on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500,null=True)
    mobile = models.CharField(max_length=20,null=True)
    order_date= models.DateField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)


class Feedback(models.Model):
    name=models.CharField(max_length=40)
    feedback=models.CharField(max_length=500)
    date= models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name
