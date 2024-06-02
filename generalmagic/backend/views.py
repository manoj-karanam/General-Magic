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
from backend.models import Registration, Experience



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
    

@csrf_exempt
@require_http_methods(["POST"])
def add_experience(request):
    try:
        data = json.loads(request.body)
        experience_data = data['experience']
        user_id = experience_data['user_id']
        
        try:
            user = Registration.objects.get(pk=user_id)
        except Registration.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)
        
        experience = Experience.objects.create(
            user=user,
            title=experience_data['title'],
            employment_type=experience_data['employment_type'],
            company_name=experience_data['company_name'],
            location=experience_data['location'],
            location_type=experience_data['location_type'],
            start_date=experience_data['start_date'],
            end_date=experience_data.get('end_date'),
            job_description=experience_data['job_description'],
            skills=experience_data['skills']
        )

        return JsonResponse({"message": "Experience added successfully"}, status=201)
    except KeyError:
        return JsonResponse({"error": "Bad request"}, status=400)

@csrf_exempt
@require_http_methods(["POST"])
def edit_experience(request, experience_id):
    try:
        data = json.loads(request.body)
        experience_data = data['experience']
        
        try:
            experience = Experience.objects.get(pk=experience_id)
        except Experience.DoesNotExist:
            return JsonResponse({"error": "Experience not found"}, status=404)
        
        experience.title = experience_data.get('title', experience.title)
        experience.employment_type = experience_data.get('employment_type', experience.employment_type)
        experience.company_name = experience_data.get('company_name', experience.company_name)
        experience.location = experience_data.get('location', experience.location)
        experience.location_type = experience_data.get('location_type', experience.location_type)
        experience.start_date = experience_data.get('start_date', experience.start_date)
        experience.end_date = experience_data.get('end_date', experience.end_date)
        experience.job_description = experience_data.get('job_description', experience.job_description)
        experience.skills = experience_data.get('skills', experience.skills)
        
        experience.save()

        return JsonResponse({"message": "Experience updated successfully"}, status=200)
    except KeyError:
        return JsonResponse({"error": "Bad request"}, status=400)
    
   
    

