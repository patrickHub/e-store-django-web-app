from csv import DictReader

from django.core.management import BaseCommand

from store.models import Product, Category

CATEGORY_IMAGE_NAMES = {
    'Bubbelgum Crush': 'bubbelgum_crush.jpg',
    'Candy Ice Blast': 'candy_ice_blast.jpg',
    'Cherry Cola': 'cherry_cola.jpg',
    'Energy Flavour': 'energy_flavour.jpg',
    'Fruit Punch': 'fruit_punch.jpg',
    'Icy Blue Raz': 'icy_blue_raz.jpg',
    'Muscle Growth': 'muscle_growth.jpg',
    'Before the Training': 'before_the_training.jpg'
}

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
        for name in CATEGORY_IMAGE_NAMES.keys():
            category = Category(categoryName=name)
            category.categoryImgPath = CATEGORY_IMAGE_NAMES[name]
            category.save()

        print('Loading product data from csv file')
        for line in DictReader(open('./product_data.csv')):
            product = Product()
            product.productName = line['productName']
            product.productPrice = line['productPrice']
            product.productDescription = line['productDescription']
            product.productImgPath = line['productImgPath']
            product.category = Category.objects.get(
                categoryName=line['productCategory'])
            product.save()
