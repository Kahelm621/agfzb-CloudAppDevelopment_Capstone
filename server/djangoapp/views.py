from django.shortcuts import render

def index(request):
    return render(request, 'djangoapp/index.html')

def about(request):
    return render(request, 'djangoapp/about.html')

def contact(request):
    return render(request, 'djangoapp/contact.html')

def login_request(request):
    # Implement your login logic here
    return render(request, 'djangoapp/login.html')

def logout_request(request):
    # Implement your logout logic here
    return render(request, 'djangoapp/logout.html')

def registration_request(request):
    # Implement your registration logic here
    return render(request, 'djangoapp/registration.html')

def get_dealer_details(request, dealer_id):
    # Implement your dealer details logic here
    return render(request, 'djangoapp/dealer_details.html')

def add_review(request, dealer_id):
    # Implement your review submission logic here
    return render(request, 'djangoapp/add_review.html')

from django.shortcuts import render

def get_dealerships(request):
    # Implement your logic to retrieve dealerships here
    context = {}  # You can pass any context data you need
    return render(request, 'djangoapp/index.html', context)


