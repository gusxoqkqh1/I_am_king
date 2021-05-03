import json
import jwt
import bcrypt
import re

from django.views import View
from django.http import JsonResponse, HttpResponse
from my_settings import SECRET_KEY

from .models import User

class SignUpView(View):
    def post(self, request):
        try :

            data = json.loads(request.body)

            email    = data['email']
            password = data['password']
            name     = data['name']

            
            email_validator    = re.compile('^[a-zA-Z0-9+-_.]+@[a-z]+.[a-z]+$')
            password_validator = re.compile('^\d{5,15}$')
            
#            if not email or not password or not name :
#                return JsonResponse({"error":"CHECK_YOUR_INPUT"}, status=400)
                
            
            if User.objects.filter(email=email).exists():
                return JsonResponse({"error":"EMAIL_EXIST"}, status=400)
            
#            if email_validator.match(email):
#                return JsonResponse({'message': 'INVALID_EMAIL_FORMAT'}, status=400)
            
            if password_validator.match(password):
                return JsonResponse({'message': 'INVALID_EMAIL_FORMAT'}, status=400)
            
            hashed_password = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt()).decode('utf-8')
            User.objects.create(
                email = email,
                password = hashed_password,
                name    = name,
                    )
            
            return HttpResponse(status=200)
        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)


class SignInView(View):
    def post(self, request):
        try :

            data =json.loads(request.body)

            email    = data['email']
            password = data['password']
            
            user = User.objects.get(email = email)
            
            if not email or not password : 
                return JsonResponse({"error":"CHECK_YOUR_INPUT"}, status=404)

            if not User.objects.filter(email=email).exists():
                return JsonResponse({'MESSAGE' : 'INVALID USER'}, status=404)
                
            if not bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({'error':'WRONG PASSWORD'}, status=400)

            access_token = jwt.encode({'user_id':user.id}, SECRET_KEY, ALGORITHM='HS256')

            return JsonResponse({"message":'SUCCESS', 'access_token':access_token},status=200)

        except KeyError:
            return JsonResponse({'error':'KEY ERROR'},status=400)
