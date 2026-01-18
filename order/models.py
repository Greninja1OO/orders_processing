from django.db import models

# Create your models here.
class PlaceOrder(models.Model):
    user_id = models.IntegerField(default=0)
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address= models.CharField(max_length=255, default='Not Provided')
    payment_method = models.CharField(max_length=50, default='Not Provided')
    status = models.CharField(max_length=50, default='Pending',choices=[('Pending','Pending'),('Shipped','Shipped'),('Delivered','Delivered'),('Cancelled','Cancelled')])
    def __str__(self):
        return f"{self.item_name} - {self.quantity} @ {self.price}"

class stock(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    last_updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.item_name} - {self.quantity}"