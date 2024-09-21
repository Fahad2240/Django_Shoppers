from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import EditItemform, NewItemForm
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
@login_required
def delete(request,pk):
    item=get_object_or_404(Item,pk=pk,created_by=request.user)
    item.delete()
    return redirect('dashboard:index')

@login_required
def edit(request,pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method=='POST':
        form=EditItemform(request.POST,request.FILES)
        if form.is_valid():
            item.save()
            return redirect('item:details',pk=item.id)
    else:
        form =EditItemform(instance=item)
    return render(request,'item\item_forms.html',{'form':form,'title':'Edit Item'})


def items(request):
    category_id = request.GET.get('category', 0)  # Get the category_id from the request query parameters
    if category_id:  # If category_id is provided
        categories = category.objects.filter(category_id=category_id)  # Filter categories based on the provided category_id
    else:
        categories = category.objects.all()  # If no category_id is provided, get all categories

    items = Item.objects.filter(is_sold=False)  # Get all items that are not sold

    return render(request, 'item\items.html', {'items': items, 'categories': categories})
   