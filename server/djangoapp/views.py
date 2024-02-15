from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Dealer, Car, Review

def index(request):
    return render(request, 'djangoapp/index.html')

def about(request):
    return render(request, 'djangoapp/about.html')

def contact(request):
    return render(request, 'djangoapp/contact.html')

def login_request(request):
    if request.user.is_authenticated:
        return redirect('djangoapp:index')
    return render(request, 'djangoapp/login.html')

def logout_request(request):
    logout(request)
    return redirect('djangoapp:index')

def registration_request(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('djangoapp:index')
    else:
        form = UserCreationForm()
    return render(request, 'djangoapp/registration.html', {'form': form})

@login_required
def get_dealer_details(request, dealer_id):
    context = {}
    reviews = Review.objects.filter(dealer_id=dealer_id)
    context['reviews'] = reviews
    return render(request, 'djangoapp/dealer_details.html', context)

@login_required
def add_review(request, dealer_id):
    if request.method == 'POST':
        content = request.POST.get('content')
        purchase_check = request.POST.get('purchasecheck')
        car_id = request.POST.get('car')
        purchase_date = request.POST.get('purchasedate')
        review = Review.objects.create(dealer_id=dealer_id, content=content, purchase_check=purchase_check, car_id=car_id, purchase_date=purchase_date)
        return redirect('djangoapp:get_dealer_details', dealer_id=dealer_id)
    else:
        dealer_cars = Car.objects.filter(dealer_id=dealer_id)
        return render(request, 'djangoapp/add_review.html', {'cars': dealer_cars})

def get_dealerships(request):
    context = {}
    dealerships = get_dealers_from_cf()  # Assuming this function retrieves dealer information
    context['dealership_list'] = dealerships
    return render(request, 'djangoapp/index.html', context)







