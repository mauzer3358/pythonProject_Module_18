from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def main_page(request):
    return render(request, 'main_template.html')

def shop_page(request):
    title = 'Shop'
    item1 = "Atomic Heart"
    item2 = "Cyberpunk 2077"
    item3 = "PayDay 2"
    context = {
        'title': title,
        'item1': item1,
        'item2': item2,
        'item3': item3
    }
    return render(request, 'shop_template.html', context)

def cart_page(request):
    return render(request, 'cart_template.html')