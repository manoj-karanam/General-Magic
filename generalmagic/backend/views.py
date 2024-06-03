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
from backend.models import Registration, UserDetails, Experience



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

@csrf_exempt
@require_http_methods(["POST"])
def add_experience(request):
    try:
        data = json.loads(request.body)
        
        # Extracting data from the request JSON
        user_id = data.get('user_id')
        title = data.get('title')
        employment_type = data.get('employment_type')
        company_name = data.get('company_name')
        location = data.get('location')
        location_type = data.get('location_type')
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        job_description = data.get('job_description')
        skills = data.get('skills')
        
        # Create the experience object
        experience = Experience.objects.create(
            user_id=user_id,
            title=title,
            employment_type=employment_type,
            company_name=company_name,
            location=location,
            location_type=location_type,
            start_date=start_date,
            end_date=end_date,
            job_description=job_description,
            skills=skills
        )
        
        # Return success response
        return JsonResponse({"message": "Experience added successfully"}, status=201)
    
    except Exception as e:
        # Return error response if any exception occurs
        return JsonResponse({"error": str(e)}, status=400)
    

@csrf_exempt
@require_http_methods(["PUT"])
def edit_experience(request, user_id):
    try:
        # Retrieve the experience object to be edited based on user_id
        experience = Experience.objects.get(user_id=user_id)
        
        # Load the JSON data from the request body
        data = json.loads(request.body)
        
        # Update the fields if they are present in the request data
        if 'title' in data:
            experience.title = data['title']
        if 'employment_type' in data:
            experience.employment_type = data['employment_type']
        if 'company_name' in data:
            experience.company_name = data['company_name']
        if 'location' in data:
            experience.location = data['location']
        if 'location_type' in data:
            experience.location_type = data['location_type']
        if 'start_date' in data:
            experience.start_date = data['start_date']
        if 'end_date' in data:
            experience.end_date = data['end_date']
        if 'job_description' in data:
            experience.job_description = data['job_description']
        if 'skills' in data:
            experience.skills = data['skills']
        
        # Save the changes
        experience.save()
        
        # Return success response
        return JsonResponse({"message": "Experience updated successfully"}, status=200)
    
    except Experience.DoesNotExist:
        # Return error response if experience does not exist
        return JsonResponse({"error": "Experience not found for user_id"}, status=404)
    
    except Exception as e:
        # Return error response if any other exception occurs
        return JsonResponse({"error": str(e)}, status=400)