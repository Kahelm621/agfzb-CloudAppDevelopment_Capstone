from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from .models import Dealer

def get_dealerships(request):
    if request.method == "GET":
        url = "your-URL-implemented-using-CLI/dealerships/get"
        dealerships = get_dealers_from_cf(url)
        dealer_names = [dealer.short_name for dealer in dealerships]
        return JsonResponse(dealer_names, safe=False)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def registration_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
        else:
            try:
                user = User.objects.create_user(username=username, password=password)
                messages.success(request, 'User created successfully. Please log in.')
                return redirect('login')
            except Exception as e:
                messages.error(request, f'An error occurred: {e}')
    return render(request, 'registration.html')

def index_view(request):
    context = {}
    return render(request, 'index.html', context)

def get_dealer_details(request, dealer_id):
    dealer = get_object_or_404(Dealer, id=dealer_id)
    reviews = dealer.reviews.all()
    context = {'dealer': dealer, 'reviews': reviews}
    return render(request, 'dealer_details.html', context)

def add_review(request, dealer_id):
    dealer = get_object_or_404(Dealer, id=dealer_id)
    if request.method == 'GET':
        context = {'dealer': dealer}
        return render(request, 'add_review.html', context)
    elif request.method == 'POST':
        # Process form submission and save review
        # Assuming 'Review' model exists and 'review_text' is a field in the model
        review_text = request.POST.get('review_text')
        dealer.reviews.create(review_text=review_text)
        return HttpResponseRedirect(reverse('dealer_details', args=[dealer_id]))



