import os
import django
import sys
import csv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE_DIR)

os.chdir("..")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wagrano.settings")
django.setup()

from products.models import *

with open('./db_upload/Category.csv', newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for data in csv_reader:
        Category.objects.create(
                name      = data['name'],
                image_url = data['image_url']
                )
with open('./db_upload/Destination.csv', newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for data in csv_reader:
        Destination.objects.create(
                name = data['name']
                )

with open('./db_upload/CategoryDestination.csv', newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for data in csv_reader:
        CategoryDestination.objects.create(
                category_id    = data['category_id'],
                destination_id = data['destination_id'],
                )

with open('./db_upload/City.csv', newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for data in csv_reader:
        City.objects.create(
                name =data['name'],
                )

with open('./db_upload/District.csv', newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for data in csv_reader:
        District.objects.create(
                name    = data['name'],
                city_id = data['city_id'],
                )

with open('./db_upload/Product.csv', newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for data in csv_reader:
        Product.objects.create(
                name           = data['name'],
                star_rating    = data['star_rating'],
                rating         = data['rating'],
                description    = data['description'],
                address        = data['address'],
                latitude       = data['latitude'],
                longitude      = data['longitude'],
                price          = data['price'],
                category_id    = data['category_id'],
                destination_id = data['destination_id'],
                city_id        = data['city_id'],
                district_id    = data['district_id'],
                )

with open('./db_upload/ProductImage.csv', newline='') as csvfile:                        
    csv_reader = csv.DictReader(csvfile)                                       
    for data in csv_reader:
        ProductImage.objects.create(
                image_url = data['image_url'],
                product_id = data['product_id'],
                )

with open('./db_upload/ServiceCategory.csv', newline='') as csvfile:                   
    csv_reader = csv.DictReader(csvfile)                                           
    for data in csv_reader:
        ServiceCategory.objects.create(
                name = data['name'],
                    )

with open('./db_upload/Convenience.csv', newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for data in csv_reader:
        Convenience.objects.create(
                name = data['name'],
                service_category_id = data['service_category_id'],
                )

with open('./db_upload/ProductConvenience.csv', newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for data in csv_reader:
        ProductConvenience.objects.create(
                product_id  = data['product_id'],
                convenience_id = data['convenience_id'],
                )



print("SUCCESS")
