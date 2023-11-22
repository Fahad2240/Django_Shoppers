from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import NewItemForm
def details(request,pk):
    item=get_object_or_404(Item,pk=pk)
    # print(item.id)
    related_items=Item.objects.filter(category=item.category,is_sold=False).exclude(pk=pk)
    # set=item.id
    # print(related_items)
    return render(request,'item\details.html',{'item':item,'related_items':related_items})
# '@' This is a decorator 
@login_required
def add_new(request):
    if request.method=='POST':
        form=NewItemForm(request.POST,request.FILES)
        if form.is_valid():
            item=form.save(commit=False)
            item.created_by=request.user
            item.save()
            return redirect('item:details',pk=item.id)
    else:
        form = NewItemForm()
    return render(request,'item\item_forms.html',{'form':form,'title':'Add New Item'})
# Create your views here.
