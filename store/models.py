from django.db import models


class Category(models.Model):

    categoryID = models.AutoField(primary_key=True)
    categoryName = models.CharField(max_length=30)


class Product(models.Model):

    productID = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=30)
    productPrice = models.FloatField()
    productDescription = models.TextField()
    productImgPath = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, db_column='categoryID', related_name='+', on_delete=models.CASCADE)
