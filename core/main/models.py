from django.db import models

# Create your models here.
class ItemType(models.Model):
    name = models.CharField('ItemType name', max_length=30)
    img = models.ImageField('ItemType image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ItemType'
        verbose_name_plural = 'ItemTypes'

class Category(models.Model):

    itemtype = models.ManyToManyField(ItemType, related_name='Item_Category')
    name = models.CharField('Category name', max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Mark(models.Model):

    category = models.ManyToManyField(Category, related_name='Category_Mark')
    name = models.CharField('Mark name', max_length=30)
    img = models.ImageField('Mark image', upload_to='media')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Mark'
        verbose_name_plural = 'Marks'

class Product(models.Model):
    mark = models.ManyToManyField(Mark, related_name='Mark_Product')
    name = models.CharField('Product name', max_length=30)
    img = models.ImageField('Product image', upload_to='media')
    price = models.IntegerField('Product price')
    about = models.TextField('Product about')
    history = models.TextField('Product history')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'