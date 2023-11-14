from django.shortcuts import render,get_object_or_404
from .models import *

def details(request,id):
    item=get_object_or_404(Item,pk=id)
    related_items=Item.objects.filter(category=item.category,is_sold=False).exclude(pk=id)
    # set=item.id
    print(related_items)
    return render(request,'details.html',{'item':item,'related_items':related_items})
    
# Create your views here.
