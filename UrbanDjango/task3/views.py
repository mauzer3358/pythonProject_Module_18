from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def main_page(request):
    return render(request, 'main_template.html')

def shop_page(request):
    return render(request, 'shop_template.html')

def cart_page(request):
    return render(request, 'cart_template.html')