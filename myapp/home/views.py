from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from myapp.item.models import *

# Create your views here.
def index(request):
    product = Product.objects.all()
    ingredient = Ingredient.objects.all()
    Category = {'product':product,'ingredient':ingredient}
    return render(request, 'index2.html', Category)