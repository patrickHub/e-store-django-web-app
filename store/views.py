from django.shortcuts import render

from .models import Category, Product
from .forms import AddToCartForm


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
        # get the  first four products of the same category
        products = Product.objects.filter(category_id=product.category_id)
        # find 'productID' category
        category = Category.objects.get(categoryID=product.category_id)
        addToCartForm = None

        # check if it is a post request
        if req.method == 'POST':
            # populate the addToCartForm with data request
            addToCartForm = AddToCartForm(req.POST)
            if addToCartForm.is_valid():
                print('This is the input quantity {}'.format(
                    addToCartForm.cleaned_data['quantity']))
            # it is a GET request
        else:
            # create a blank addToCart form
            addToCartForm = AddToCartForm()

        data = {
            'product': product,
            'products': products,
            'category': category,
            'addToCartForm': addToCartForm
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
