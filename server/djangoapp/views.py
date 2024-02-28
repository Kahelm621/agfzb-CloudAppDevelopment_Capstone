from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# About view
def about(request):
    # Render the about page
    return render(request, 'djangoapp/about.html')

# Contact view
def contact(request):
    # Render the contact page
    return render(request, 'djangoapp/contact.html')

# Registration view
def registration_request(request):
    if request.method == "POST":
        # Handle registration form submission
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        # Create a new user
        user = User.objects.create_user(username, email, password)
        user.save()
        messages.success(request, "Account created successfully. Please log in.")
        return redirect('djangoapp:login')  # Redirect to login page after registration
    # Render the registration page
    return render(request, 'djangoapp/registration.html')

# Login view
def login_request(request):
    if request.method == "POST":
        # Handle login form submission
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # If user is authenticated, log them in
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            return redirect('djangoapp:index')  # Redirect to index page after login
        else:
            # If authentication fails, display error message
            messages.error(request, "Invalid username or password.")
    # Render the login page
    return render(request, 'djangoapp/login.html')

# Logout view
def logout_request(request):
    # Handle logout request
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('djangoapp:index')  # Redirect to index page after logout

# Index view
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        # Retrieve dealerships and render index page
        # Add logic to retrieve dealerships here
        return render(request, 'djangoapp/index.html', context)

# Dealer details view
def get_dealer_details(request, dealer_id):
    # Retrieve dealer details and render dealer details page
    # Add logic to retrieve dealer details here
    return render(request, 'djangoapp/dealer_details.html')

# Add review view
def add_review(request, dealer_id):
    # Handle adding a review for a dealer
    if request.method == "POST":
        # Process review form submission
        # Add logic to save the review for the dealer
        return redirect('djangoapp:dealer_details', dealer_id=dealer_id)  # Redirect to dealer details page after review submission
    # Render the add review page
    return render(request, 'djangoapp/add_review.html')

