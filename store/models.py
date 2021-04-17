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
    item = models.ManyToManyField(Item, verbose_name='آیتم ها')

    def __str__(self):
        return self.product_name
