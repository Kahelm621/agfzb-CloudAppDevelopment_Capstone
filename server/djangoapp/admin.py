from django.contrib import admin
from .models import CarMake, CarModel, Course, Instructor, Lesson

class CourseAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'name', 'description']

class InstructorAdmin(admin.ModelAdmin):
    fields = ['user', 'full_time']

class LessonInline(admin.StackedInline):
    model = Lesson 
    extra = 5

class CourseAdminWithLesson(admin.ModelAdmin):
    fields = ['pub_date', 'name', 'description']
    inlines = [LessonInline]

class CarModelInline(admin.TabularInline):
    model = CarModel

class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]

admin.site.register(Course, CourseAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel)
admin.site.register(Lesson)