from csv import DictReader

from django.core.management import BaseCommand

from store.models import Product, Category

CATEGORY_NAMES = [
    'Bubbelgum Crush',
    'Candy Ice Blast',
    'Cherry Cola',
    'Energy Flavour',
    'Fruit Punch',
    'Icy Blue Raz'
]

ALREADY_LOADED_ERROR_MESSAGE = """
If you need to reload the product data from the CSV file,
first delete the database from mysql server and create a new one with the same name.
Then, run `python manage.py migrate` to create empty tables inside the new database"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from product_data.csv into our Product model"

    def handle(self, *args, **options):
        if Category.objects.exists() or Category.objects.exists():
            print('Product already loaded...existing.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print('Creating category data')
        for name in CATEGORY_NAMES:
            category = Category(categoryName=name)
            category.save()
        print('Loading product data from csv file')
        for line in DictReader(open('./product_data.csv')):
            product = Product()
            product.productName = line['productName']
            product.productPrice = line['productPrice']
            product.productDescription = line['productDescription']
            product.productImgPath = line['productImgPath']
            product.category = Category.objects.get(
                categoryName=line['category'])
            product.save()
