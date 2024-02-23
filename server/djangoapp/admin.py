from django.contrib import admin
from .models import CarMake, CarModel


class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1

class CarModelAdmin(admin.ModelAdmin):
    # Define the admin representation for CarModel model
    list_display = ('name', 'make', 'type', 'year', 'dealer_id')
    list_filter = ('make', 'type', 'year')
    search_fields = ('name', 'make__name', 'type')

class CarMakeAdmin(admin.ModelAdmin):
    # Define the admin representation for CarMake model
    list_display = ('name', 'description')
    search_fields = ('name',)
    inlines = [CarModelInline]

# Register CarMake and CarModel models with their respective admins
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)


