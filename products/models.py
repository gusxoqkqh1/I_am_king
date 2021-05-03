from django.db import models

class Category(models.Model):
    name      = models.CharField(max_length=45)
    image_url = models.URLField(max_length=2000)
    destination = models.ManyToManyField('Destination', through='CategoryDestination')

    class Meta:
        db_table = 'categories'

class Destination(models.Model):
    name      = models.CharField(max_length=45)
    image_url = models.URLField(max_length=2000)

    class Meta:
        db_table = 'destinations'

class CategoryDestination(models.Model):
    category    = models.ForeignKey('Category', on_delete=models.CASCADE)
    destination = models.ForeignKey('Destination', on_delete=models.CASCADE)

    class Meta:
        db_table = 'category_destinations'

class City(models.Model):
    name = models.CharField(max_length=45, null=True)

    class Meta:
        db_table = 'cities'

class District(models.Model):
    name = models.CharField(max_length=45)
    city = models.ForeignKey('City', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'districts'

class Product(models.Model):
    name        = models.CharField(max_length=45)
    star_rating = models.SmallIntegerField(default=0)
    rating      = models.DecimalField(max_digits=3, decimal_places=1)
    description = models.TextField()
    address     = models.CharField(max_length=100)
    latitude    = models.DecimalField(max_digits=20, decimal_places=17)
    longitude   = models.DecimalField(max_digits=20, decimal_places=17)
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    category    = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    destination = models.ForeignKey('Destination', on_delete=models.SET_NULL, null=True)
    city        = models.ForeignKey('City', on_delete=models.SET_NULL, null=True)
    district    = models.ForeignKey('District', on_delete=models.SET_NULL, null=True)
    convenience = models.ManyToManyField('Convenience', through='ProductConvenience')

    class Meta:
        db_table = 'products'

class ProductImage(models.Model):
    image_url = models.URLField(max_length=2000)
    product   = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'product_images'

class Convenience(models.Model):
    name             = models.CharField(max_length=45)
    service_category = models.ForeignKey('ServiceCategory', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'conveniences'

class ProductConvenience(models.Model):
    product     = models.ForeignKey('Product', on_delete=models.CASCADE)
    convenience = models.ForeignKey('Convenience', on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_conveniences'

class ServiceCategory(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'service_categories'
