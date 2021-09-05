from django.db import models
# from django.contrib.auth.models import User
# from app_data_off.models import Product


# Create your models here.

# class Substitut(models.Model):
#     """ table between Product and User. """
#
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart")
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.user
#
#
# class SaveSubstitut(models.Model):
#     orderitems = models.ManyToManyField(Substitut)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     ordered = models.BooleanField(default=False)
#     created = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.orderitems
