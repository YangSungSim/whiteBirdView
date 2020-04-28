from django.contrib import admin
from .models import *
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','imageid','name']

admin.site.register(Product,ProductAdmin)

class IngredientAdmin(admin.ModelAdmin):
    list_display = ['oily','dry','sensitive']

admin.site.register(Ingredient,IngredientAdmin)