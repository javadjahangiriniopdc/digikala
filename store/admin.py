from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Customer)
admin.site.register(GroupProduct)
admin.site.register(Product)
admin.site.register(Item)

admin.site.register(ProductItemValue)
admin.site.register(OrderMaster)
