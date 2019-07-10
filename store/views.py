from django.shortcuts import render

from .models import Category


def index(req):

    categories = Category.objects.all()
    data = {
        'categories': categories
    }
    return render(req, 'index.html', data)
