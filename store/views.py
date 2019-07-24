from django.shortcuts import render

from .models import Category, Product


def index(req):

    # get all categories from db
    categories = Category.objects.all()
    data = {
        'categories': categories
    }
    # pass control to index.html template
    return render(req, 'index.html', data)


def productsPerCategory(req, categoryID):
    try:
        # find 'categoryID' category
        category = Category.objects.get(categoryID=categoryID)
        # find 'categoryID' products
        products = Product.objects.filter(category_id=categoryID)
        data = {
            'products': products,
            'category': category
        }
        # pass control to product_cat.html template
        return render(req, 'product_cat.html', data)
    except Category.DoesNotExist:
        # if categoryID does not exist then return all products
        products = Product.objects.all()
        data = {
            'products': products
        }
        return render(req, 'product_cat.html', data)


def productDetail(req, productID):
    try:
        # find 'productID' product
        product = Product.objects.get(productID=productID)
        products = Product.objects.filter(category_id=product.category_id)
        # find 'productID' category
        category = Category.objects.get(categoryID=product.category_id)
        data = {
            'product': product,
            'products': products,
            'category': category
        }
        # pass control to product_detail.html template
        return render(req, 'product_detail.html', data)
    except Product.DoesNotExist:
        # if the productID does not exist then return all products
        products = Product.objects.all()
        data = {
            'products': products
        }
        return render(req, 'product_cat.html', data)
