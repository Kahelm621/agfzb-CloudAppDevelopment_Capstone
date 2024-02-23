from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'

urlpatterns = [
    # Path for registration
    path('registration/', views.registration_view, name='registration'),

    # Path for login
    path('login/', views.login_view, name='login'),

    # Path for logout
    path('logout/', views.logout_view, name='logout'),

    # Default index path
    path('', views.index_view, name='index'),

    # Additional path for get_dealerships view
    path('get_dealerships/', views.get_dealerships, name='get_dealerships'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urls.py

from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'

urlpatterns = [
    path(route='', view=views.get_dealerships, name='index')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
