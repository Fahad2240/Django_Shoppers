from django.shortcuts import  render
from .forms import SignupForm
from item.models import Item, category

# Create your views here.
def index(request):
    items=Item.objects.filter(is_sold=False)[:9]
    categories=category.objects.all()
    return render(request,'index.html',{
        'categories':categories,'items':items})
    
def contact(request):
    return render(request,'contact.html')

def signup(request):
    form=SignupForm()
    return render(request,'signup.html',{form:'form'})
# def details(request,pk):
#     item=get_object_or_404(Item,pk=pk)
#     return render(request,'details.html',{'item':item})