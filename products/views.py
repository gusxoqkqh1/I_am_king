import json

from django.views import View
from django.http import HttpResponse, JsonResponse

from .models import *
class ProductDetailView(View):
    def get(self, request,product_id= None):

        try :
            products = Product.objects.get(id=1)
            productview = [
                {
                    'id'          : product.id,
                    'name'        : product.name,
                    'star-rating' : product.star_rating,
                    'rating'      : product.rating,
                    'address'     : product.address,
                    'image_url'   : [image.image_url for image in products.productimage_set.all()],
                    'description' : product.description,
                    'address'     : product.address,
                    'latitude'    : product.latitude,
                    'longitude'   : product.longitude,
                    'price'       : product.price,
                    'convenience' : [service.name for service in products.convenience.all()],
                } for product in Product.objects.all()]
            return JsonResponse({'product':productview},status=200)
        except Exception as e:
            return JsonResponse({'message':f"error by {e}"}, status=400)
class MainView(View):
    def get(self, request):
        try:
            mainviews = [
                {
                    'id'          : product.id,
                    'name'        : product.name,
                    'star-rating' : product.star_rating,
                    'rating'      : product.rating,
                    'description' : product.description,
                    'address'     : product.address,
                    'latitude'    : product.latitude,
                    'longitude'   : product.longitude,
                    'price'       : product.price,
                    'categorys'    :
                        [{
                        'id'  : product.category.id,
                        'name':  product.category.name,
                        'image_url' : product.category.image_url
                        }],
                    'destination' : [{
                        'id'        : product.destination.id,
                        'name'      : product.destination.name,
                        'image_url' : product.destination.image_url
                        }],
                    'city'        : product.city.name,
                    'district'    : product.district.name,
                    'convenience' : [service.name for service in Product.objects.get(id = 1).convenience.all()]
                        }  for product in Product.objects.all()]
            return JsonResponse({'product':mainviews},status=200)
        except Exception as e:
            return JsonResponse({'message':f"error by {e}"}, status=400)
# Create your views here.
