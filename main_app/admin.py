from django.contrib import admin
from .models import Recipe, Meal, Tag, Category

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Meal)
admin.site.register(Tag)
admin.site.register(Category)