from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Customer(models.Model):
    class Meta:
        verbose_name = 'مشتری'
        verbose_name_plural = 'مشتریان'

    user = models.OneToOneField(User, on_delete=models.PROTECT, verbose_name='کاربر')
    customer_name = models.CharField('نام مشتری', max_length=50, null=False, blank=False)
    customer_family = models.CharField('نام خانوادگی مشتری', max_length=50, null=False, blank=False)

    def __str__(self):
        return self.customer_name + '-' + self.customer_family


class Item(models.Model):
    class Meta:
        verbose_name = ' ایتم'
        verbose_name_plural = '  آیتم ها'

    item_name = models.CharField('نام آیتم', max_length=50, null=False, blank=False)
    item_description = models.CharField('توضیحات', max_length=500, null=True, blank=True)

    def __str__(self):
        return self.item_name


class GroupProduct(models.Model):
    class Meta:
        verbose_name = ' گروه محصول'
        verbose_name_plural = ' گروه محصولات'

    groupProduct = models.CharField('نام آیتم', max_length=50, null=False, blank=False)
    groupProduct_description = models.CharField('توضیحات', max_length=500, null=True, blank=True)

    def __str__(self):
        return self.groupProduct


class Product(models.Model):
    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    groupProduct = models.ForeignKey(GroupProduct, null=False, on_delete=models.PROTECT, default='',
                                     verbose_name='گروه محصولات')
    product_name = models.CharField('نام محصول', max_length=50, null=False, blank=False)

    def __str__(self):
        return self.product_name


class ProductItem(models.Model):
    class Meta:
        verbose_name = 'مقدار ایتم محصول'
        verbose_name_plural = 'مقادیر ایتم های محصولات'

    item = models.ForeignKey(Item, verbose_name='ایتم', on_delete=models.PROTECT)
    product = models.ForeignKey(Product, verbose_name='محصولات', on_delete=models.PROTECT)

    def __str__(self):
        return self.product.product_name + "-" + self.item.item_name


class OrderMaster(models.Model):
    class Meta:
        verbose_name = 'سفارش محصول'
        verbose_name_plural = 'سفارشات محصولات'

    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, verbose_name='مشتری')
    create_at = models.DateTimeField(default=datetime.now(), verbose_name='تاریخ ایجاد')

    def __str__(self):
        return self.customer.__str__() + "-" + self.create_at.__str__()


class OrderMasterDetials(models.Model):
    class Meta:
        verbose_name = 'ریز سفارش محصول'
        verbose_name_plural = 'ریز سفارشات محصولات'

    orderMaster = models.ForeignKey(OrderMaster, verbose_name='آیتم محصول', on_delete=models.PROTECT)
    productItem = models.ForeignKey(ProductItem, verbose_name='آیتم محصول', on_delete=models.PROTECT)
    value = models.CharField(max_length=64, verbose_name='مقادیر')

    def __str__(self):
        return self.orderMaster.__str__() + "-" + self.productItem.__str__() + self.value
