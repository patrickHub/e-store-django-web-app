from django.shortcuts import render
from django.db.models import Sum

from .models import Category, Product, Cart, ProductCart
from .forms import AddToCartForm
from store.dto.itemCart import ItemCart
from store.serializer.serializer import Serilizer


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
        products = Product.objects.filter(
            category_id=product.category_id).exclude(productID=productID)[:4]
        # find 'productID' category
        category = Category.objects.get(categoryID=product.category_id)
        # get  request session
        session = req.session
        addToCartForm = None
        productCarts = None
        cartID = None

        # check weither the cartID exist in session
        if 'cartID' in session:
            # get the cartID from the session
            cartID = session['cartID']
        else:
            # the cart does not exist then create and save it to DB
            cart = Cart()
            cart.save()
            cartID = cart.cartID
            # save the cartID to session
            req.session['cartID'] = cartID

        # check if it is a post request
        if req.method == 'POST':
            # populate the addToCartForm with data request
            addToCartForm = AddToCartForm(req.POST)
            if addToCartForm.is_valid():
                # get product quantity
                quantity = addToCartForm.cleaned_data['quantity']

                try:
                    # check weither the productCart exist in DB
                    productCart = ProductCart.objects.get(
                        cartID=cartID, productID=product.productID)
                    # the productCart exist then update its quantity
                    productCart.quantity += quantity

                except ProductCart.DoesNotExist:
                    # the productCart does not exist then create it
                    productCart = ProductCart()
                    productCart.cartID = Cart.objects.get(cartID=cartID)
                    productCart.productID = product
                    productCart.quantity = quantity

                # save/update the productCart to DB
                productCart.save()

        else:  # it is a GET request
            # create a blank addToCart form
            addToCartForm = AddToCartForm()

        # get all 'cartID' productCart
        productCarts = ProductCart.objects.filter(
            cartID=cartID).aggregate(totalQuantity=Sum('quantity'))

        data = {
            'product': product,
            'products': products,
            'category': category,
            'addToCartForm': addToCartForm,
            'productCarts': productCarts
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
