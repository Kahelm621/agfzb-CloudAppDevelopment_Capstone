from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # path for about view
    path('about/', views.about, name='about'),

    # path for contact us view
    path('contact/', views.contact, name='contact'),

    # path for registration
    path('registration/', views.registration_request, name='registration'),

    # path for login
    path('login/', views.login_request, name='login'),

    # path for logout
    path('logout/', views.logout_request, name='logout'),

    # path for dealer reviews view
    path('dealer/<int:dealer_id>/', views.get_dealer_details, name='dealer_details'),

    # path for add a review view
    path('dealer/<int:dealer_id>/add_review/', views.add_review, name='add_review'),

    # path for index view (should be at the end)
    path('', views.get_dealerships, name='index'),
] 

# Add the signup URL pattern
urlpatterns += [
    path('signup/', views.signup, name='signup'),
]

# Serve media files in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
