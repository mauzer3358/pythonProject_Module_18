from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def main_page(request):
    return render(request, 'main_template.html')

def shop_page(request):
    games = ["Atomic Heart","Cyberpunk 2077", "PayDay 2"]
    # item1 = "Atomic Heart"
    # item2 = "Cyberpunk 2077"
    # item3 = "PayDay 2"
    context = {
        'games': games
    }
    return render(request, 'shop_template.html', context)

def cart_page(request):
    return render(request, 'cart_template.html')
