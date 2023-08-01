from django.shortcuts import render

from item.models import Item, category

# Create your views here.
def index(request):
    items=Item.objects.filter(is_sold=False)[:9]
    categories=category.objects.all()
    return render(request,'index.html',{
        'categories':categories,'item':items})
def contact(request):
    return render(request,'contact.html')