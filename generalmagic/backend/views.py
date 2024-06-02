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
from backend.models import Registration, UserDetails



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
def add_user_details(request):
    try:
        data = json.loads(request.body)
        user_data = data['user_details']
        first_name = user_data['first_name']
        middle_name = user_data.get('middle_name', None)
        last_name = user_data['last_name']
        pronouns = user_data.get('pronouns', None)
        birthday = datetime.strptime(user_data['dateOfBirth'], '%Y-%m-%d').date()
        phone_number = user_data.get('phone_number', None)
        address = user_data.get('address', None)

        # Create UserDetails object
        UserDetails.objects.create(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            pronouns=pronouns,
            birthday=birthday,
            phone_number=phone_number,
            address=address
        )

        return JsonResponse({"message": "User details added successfully"}, status=201)
    except KeyError:
        return JsonResponse({"error": "Bad request"}, status=400)

@csrf_exempt
@require_http_methods(["PUT"])
def edit_user_details(request):
    try:
        data = json.loads(request.body)
        user_data = data.get('user_details')

        if 'user_id' not in user_data:
            return JsonResponse({"error": "Missing user_id field"}, status=400)
        
        user_id = user_data.get('user_id')
        user_details = UserDetails.objects.get(user_id=user_id)
        
        # updating fields
        user_details.first_name = user_data.get('first_name', user_details.first_name)
        user_details.middle_name = user_data.get('middle_name', user_details.middle_name)
        user_details.last_name = user_data.get('last_name', user_details.last_name)
        user_details.pronouns = user_data.get('pronouns', user_details.pronouns)
        if 'dateOfBirth' in user_data:
            user_details.date_of_birth = datetime.strptime(user_data.get('dateOfBirth'), '%Y-%m-%d').date()
        user_details.phone_number = user_data.get('phone_number', user_details.phone_number)
        user_details.address = user_data.get('address', user_details.address)

        user_details.save()

        return JsonResponse({"message": "user information updated successfully"}, status=200)
    except UserDetails.DoesNotExist:
        return JsonResponse({"error": "user information not found"}, status=404)
    except KeyError as e:
        return JsonResponse({"error": f"Missing field in request: {str(e)}"}, status=400)
    except ValueError as e:
        return JsonResponse({"error": str(e)}, status=400)
    except Exception as e:
        return JsonResponse({"error": f"An unexpected error occurred: {str(e)}"}, status=500)

@csrf_exempt
@require_http_methods(["GET"])
def get_user_details(request, user_id):
    try:
        # Retrieve the UserDetails object with the given user_id
        user_details = UserDetails.objects.get(user_id=user_id)
        
        # Prepare the user data to be returned in the response
        user_data = {
            "user_id": user_details.user_id,
            "first_name": user_details.first_name,
            "middle_name": user_details.middle_name,
            "last_name": user_details.last_name,
            "pronouns": user_details.pronouns,
            "birthday": str(user_details.birthday) if user_details.birthday else None,
            "phone_number": user_details.phone_number,
            "address": user_details.address
        }
        
        # Return the user data as a JSON response
        return JsonResponse({"user_details": user_data}, status=200)
    
    except UserDetails.DoesNotExist:
        # Return an error response if user details are not found
        return JsonResponse({"error": "User details not found"}, status=404)

# @csrf_exempt
# @require_http_methods(["POST"])
# def add_experience(request):
#     try:
#         data = json.loads(request.body)
#         experience_data = data['experience']
#         user_id = experience_data['user_id']
        
#         try:
#             user = Registration.objects.get(pk=user_id)
#         except Registration.DoesNotExist:
#             return JsonResponse({"error": "User not found"}, status=404)
        
#         experience = Experience.objects.create(
#             user=user,
#             title=experience_data['title'],
#             employment_type=experience_data['employment_type'],
#             company_name=experience_data['company_name'],
#             location=experience_data['location'],
#             location_type=experience_data['location_type'],
#             start_date=experience_data['start_date'],
#             end_date=experience_data.get('end_date'),
#             job_description=experience_data['job_description'],
#             skills=experience_data['skills']
#         )

#         return JsonResponse({"message": "Experience added successfully"}, status=201)
#     except KeyError:
#         return JsonResponse({"error": "Bad request"}, status=400)

# @csrf_exempt
# @require_http_methods(["POST"])
# def edit_experience(request, experience_id):
#     try:
#         data = json.loads(request.body)
#         experience_data = data['experience']
        
#         try:
#             experience = Experience.objects.get(pk=experience_id)
#         except Experience.DoesNotExist:
#             return JsonResponse({"error": "Experience not found"}, status=404)
        
#         experience.title = experience_data.get('title', experience.title)
#         experience.employment_type = experience_data.get('employment_type', experience.employment_type)
#         experience.company_name = experience_data.get('company_name', experience.company_name)
#         experience.location = experience_data.get('location', experience.location)
#         experience.location_type = experience_data.get('location_type', experience.location_type)
#         experience.start_date = experience_data.get('start_date', experience.start_date)
#         experience.end_date = experience_data.get('end_date', experience.end_date)
#         experience.job_description = experience_data.get('job_description', experience.job_description)
#         experience.skills = experience_data.get('skills', experience.skills)
        
#         experience.save()

#         return JsonResponse({"message": "Experience updated successfully"}, status=200)
#     except KeyError:
#         return JsonResponse({"error": "Bad request"}, status=400)
    
   
    

