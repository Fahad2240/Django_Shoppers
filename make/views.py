from django.shortcuts import  redirect, render
from django.urls import is_valid_path
from .forms import SignupForm
from item.models import Item, category

# Create your views here.
def index(request):
    items=Item.objects.filter(is_sold=False)[:9]
    categories=category.objects.all()
    return render(request,'make\index.html',{
        'categories':categories,'items':items})
    
def contact(request):
    return render(request,'make\contact.html')

def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form=SignupForm()
    return render(request,'make\signup.html',{'form':form})
# def details(request,pk):
#     item=get_object_or_404(Item,pk=pk)
#     return render(request,'details.html',{'item':item})