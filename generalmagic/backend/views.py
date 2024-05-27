from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
import json
from django.forms.models import model_to_dict
from datetime import datetime
from django.db import IntegrityError
from backend.models import Registration


@csrf_exempt
@require_http_methods(["POST"])
def register_user(request):
    try:
        data = json.loads(request.body)
        registration_data = data['registration']
        fullname = registration_data['fullname']
        email = registration_data['email']
        password = registration_data['password']
        confirm_password = registration_data['confirmpassword']

        if password != confirm_password:
            return JsonResponse({"error": "Password and confirm password do not match"}, status=400)
        hashed_password = make_password(password)

        try:
            Registration.objects.create(
                fullname=fullname,
                email=email,
                password=hashed_password,
            )
        except IntegrityError:
            return JsonResponse({"error": "Email already registered"}, status=400)

        return JsonResponse({"message": "User registered successfully"}, status=201)
    except KeyError:
        return JsonResponse({"error": "Bad request"}, status=400)
    

@csrf_exempt
@require_http_methods(["POST"])
def user_login(request):
    try:
        data = json.loads(request.body)
        email = data['login']['email']
        password = data['login']['password']

        try:
            user = Registration.objects.get(email=email)
            # Check if the hashed password matches the one provided by the user
            print("email : " + email)
            if check_password(password, user.password):
                # Password matches, login successful
                return JsonResponse({"message": "Login successful"}, status=200)
            else:
                # Password does not match
                return JsonResponse({"error": "Invalid credentials"}, status=400)
        except Registration.DoesNotExist:
            # User not found
            return JsonResponse({"error": "User does not exist"}, status=400)
    except KeyError:
        return JsonResponse({"error": "Bad request"}, status=400)    
    
   
    

