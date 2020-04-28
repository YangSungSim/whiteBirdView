from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .form import SkinTypeForm

from .models import *

# Create your views here.
def index(request):
    product = Product.objects.all()
    ingredient = Ingredient.objects.all()
    skintype = SkinType.objects.all()
    dry_input = skintype[0]['dry']
    oily_input = skintype[0]['oily']
    sensitive_input = skintype[0]['sensitive']
    if dry_input < oily_input:
        recommand_cos = product.order_by('-dry_score')[:10]
    elif dry_input > oily_input:
        recommand_cos = product.order_by('dry_score')[:10]
    elif (sensitive_input > dry_input) or (sensitive_input > oily_input):
        recommand_cos = product.order_by('-sensi_score')[:10]
    Category = {'product':product,'ingredient':ingredient,'skintype':skintype,'reco':recommand_cos}
    return render(request,'item/index.html',Category)

def post(request):
    form = SkinTypeForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            lotto = form.save(commit=True)
            return redirect('indexs')
    return render(request,'item/for_form.html',{'form':form})