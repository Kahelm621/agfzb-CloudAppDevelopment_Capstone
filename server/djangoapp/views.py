from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.

# Create an `about` view to render a static about page
def about(request):
    return render(request, 'djangoapp/about.html')

# Create a `contact` view to return a static contact page
def contact(request):
    return render(request, 'djangoapp/contact.html')

# Create a `login_request` view to handle sign in request
def login_request(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            return redirect('index')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'djangoapp/login.html')

# Create a `logout_request` view to handle sign out request
def logout_request(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('index')

# Create a `registration_request` view to handle sign up request
def registration_request(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username, email, password)
        user.save()
        messages.success(request, "Account created successfully. Please log in.")
        return redirect('login')
    return render(request, 'djangoapp/registration.html')

# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)

# Create a `get_dealer_details` view to render the reviews of a dealer
def get_dealer_details(request, dealer_id):
    # Implement logic to retrieve dealer details and render the reviews
    return render(request, 'djangoapp/dealer_details.html')

# Create a `add_review` view to submit a review
def add_review(request, dealer_id):
    # Implement logic to add a review for a dealer
    return HttpResponse("Review added successfully.")
