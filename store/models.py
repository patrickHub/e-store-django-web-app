from django.db import models


class Category(models.Model):

    categoryID = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=30)
    categoryImgPath = models.CharField(max_length=100, null=True)


class Product(models.Model):

    productID = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=30)
    productPrice = models.FloatField()
    productDescription = models.TextField()
    productImgPath = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, db_column='categoryID', related_name='+', on_delete=models.CASCADE)


class Cart(models.Model):
    cartID = models.AutoField(primary_key=True)


class ProductCart(models.Model):
    cartID = models.ForeignKey(
        Cart, db_column='cartID', related_name='+', on_delete=models.CASCADE)
    productID = models.ForeignKey(
        Product, db_column='productID', related_name='+', on_delete=models.CASCADE)
    quantity = models.IntegerField()
