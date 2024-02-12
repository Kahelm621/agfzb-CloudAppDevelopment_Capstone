from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout

def index(request):
    return render(request, 'djangoapp/index.html')

def about(request):
    return render(request, 'djangoapp/about.html')

def contact(request):
    return render(request, 'djangoapp/contact.html')

def login_request(request):
    # Implement your login logic here
    # For example, you can check if the user is authenticated
    if request.user.is_authenticated:
        return redirect('djangoapp:index')  # Redirect to index if already logged in
    # Your login logic here
    return render(request, 'djangoapp/login.html')

def logout_request(request):
    # Implement your logout logic here
    # For example, you can use Django's built-in logout function
    logout(request)
    return redirect('djangoapp:index')  # Redirect to index after logout

def registration_request(request):
    # Implement your registration logic here
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('djangoapp:index')  # Redirect to index page after successful sign-up
    else:
        form = UserCreationForm()
    return render(request, 'djangoapp/registration.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('djangoapp:index')  # Redirect to the index page after successful sign-up
    else:
        form = UserCreationForm()
    return render(request, 'djangoapp/registration.html', {'form': form})

def get_dealer_details(request, dealer_id):
    # Implement your dealer details logic here
    return render(request, 'djangoapp/dealer_details.html')

def add_review(request, dealer_id):
    # Implement your review submission logic here
    return render(request, 'djangoapp/add_review.html')

def get_dealerships(request):
    # Implement your logic to retrieve dealerships here
    context = {}  # You can pass any context data you need
    return render(request, 'djangoapp/index.html', context)






