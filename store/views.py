from django.shortcuts import render

from .models import Category, Product


def index(req):

    categories = Category.objects.all()
    data = {
        'categories': categories
    }
    return render(req, 'index.html', data)


def productsPerCategory(req, categoryID):
    try:
        category = Category.objects.get(categoryID=categoryID)
        products = Product.objects.filter(category_id=categoryID)
        data = {
            'products': products,
            'category': category
        }
        print("I m here")
        return render(req, 'product_cat.html', data)
    except Category.DoesNotExist:
        products = Product.objects.all()
        data = {
            'products': products
        }
        return render(req, 'product_cat.html', data)
