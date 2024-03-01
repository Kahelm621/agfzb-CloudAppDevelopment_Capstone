from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'

urlpatterns = [
    # Path for about view
    path('about/', views.about, name='about'),

    # Path for contact us view
    path('contact/', views.contact, name='contact'),

    # Path for registration
    path('registration/', views.registration_request, name='registration'),

    # Path for login
    path('login/', views.login_request, name='login'),

    # Path for logout
    path('logout/', views.logout_request, name='logout'),

    # Path for signup
    path('signup/', views.signup, name='signup'),

    # Path for index view
    path('', views.get_dealerships, name='index'),

    # Path for dealer details view
    path('dealer/<int:dealer_id>/', views.get_dealer_details, name='dealer_details'),

    # Path for add a review view
    path('dealer/<int:dealer_id>/add_review/', views.add_review, name='add_review'),

    # Static media URL configuration
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



