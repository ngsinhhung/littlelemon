from django.shortcuts import render
from .models import Menu
# Create your views here.
def home(request):
    return render(request,"index.html")

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {
        "menu": menu_data,
    }
    return render(request, "menu.html", main_data)

def display_menu_items(request, pk):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ""
    return render(request, "menu_item.html", {"menu_item": menu_item})