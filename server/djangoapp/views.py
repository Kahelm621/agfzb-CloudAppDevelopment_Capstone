from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created successfully for {username}. Please log in.")
            return redirect('djangoapp:login')  # Redirect to login page after registration
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = UserCreationForm()
    return render(request, 'djangoapp/registration.html', {'form': form})

# Login view
def login_request(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            return redirect('djangoapp:index')  # Redirect to index page after login
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'djangoapp/login.html')

# Logout view
def logout_request(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('djangoapp:index')  # Redirect to index page after logout

# Sign-up view
def signup(request):
    form = UserCreationForm()
    return render(request, 'djangoapp/signup.html', {'form': form})

# Index view
def get_dealerships(request):
    # Logic to retrieve dealerships
    return render(request, 'djangoapp/index.html')

# Dealer details view
def get_dealer_details(request, dealer_id):
    # Logic to retrieve dealer details
    return render(request, 'djangoapp/dealer_details.html')

# Add review view
def add_review(request, dealer_id):
    if request.method == "POST":
        # Logic to add a review
        return redirect('djangoapp:dealer_details', dealer_id=dealer_id)
    return render(request, 'djangoapp/add_review.html')

