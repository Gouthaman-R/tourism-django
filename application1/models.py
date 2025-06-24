

# # application1/models.py

# from django.db import models
# from django.contrib.auth.models import AbstractUser



# class User(AbstractUser):
#     age = models.IntegerField(default=0)
#     phone_number = models.CharField(max_length=15)

#     def __str__(self):
#         return self.username

# class Product(models.Model):
#     title=models.CharField(max_length=100)
#     content=models.TextField()
#     # img=models.ImageField(upload_to='images/')
#     price=models.IntegerField(max_length=100)


# class ProductImage(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
#     image = models.ImageField(upload_to='products/')

#     def __str__(self):
#         return f"Image for {self.product.title}"
    
# application1/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    age = models.IntegerField(default=0)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.username

class Product(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    price = models.IntegerField()
    
    def __str__(self):
        return self.title

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return f"Image for {self.product.title}"

class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.title}"

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)  # Set a default value

    def __str__(self):
        return f"{self.user.username}'s Cart"











# from django.db import models
# from django.contrib.auth.models import User
# from django.conf import settings



# class Order(models.Model):
#     PAYMENT_CHOICES = [
#         ('gpay', 'Google Pay'),
#         ('bank-transfer', 'Bank Transfer'),
#         ('cash-on-delivery', 'Cash on Delivery'),
#     ]

#     # user = models.ForeignKey(User, on_delete=models.CASCADE) 
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Link to the product ordered
#     payment_mode = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
#     phone_number = models.CharField(max_length=15)  # Store user’s phone number
#     total_price = models.DecimalField(max_digits=10, decimal_places=2)
#     order_date = models.DateTimeField(auto_now_add=True)  # Store the date/time of order

#     def __str__(self):
#         return f"Order {self.id} - {self.user.username} - {self.product.title}"






