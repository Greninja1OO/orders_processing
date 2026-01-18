from django.contrib import admin
from order.models import PlaceOrder, stock

# Register your models here.
admin.site.register(PlaceOrder)
admin.site.register(stock)


