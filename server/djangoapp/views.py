from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.

# About view
def about(request):
    return render(request, 'djangoapp/about.html')

# Contact view
def contact(request):
    return render(request, 'djangoapp/contact.html')

# Registration view
def registration_request(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username, email, password)
        user.save()
        messages.success(request, "Account created successfully. Please log in.")
        return redirect('djangoapp:login')
    return render(request, 'djangoapp/registration.html')

# Login view
def login_request(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            return redirect('djangoapp:index')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'djangoapp/login.html')

# Logout view
def logout_request(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('djangoapp:index')

# Index view
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)

# Dealer details view
def get_dealer_details(request, dealer_id):
    # Implement logic to retrieve dealer details and render the reviews
    return render(request, 'djangoapp/dealer_details.html')

# Add review view
def add_review(request, dealer_id):
    # Implement logic to add a review for a dealer
    return render(request, 'djangoapp/add_review.html')

