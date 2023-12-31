from django import forms
from .models import Item

FROM_INPUT_CLASSES=' w-full px-5 py-3 rounded-xl border'
class NewItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=('category','name','description','price','image') 
        widgets={
            'category': forms.Select(attrs={'class': FROM_INPUT_CLASSES}),
            'name': forms.TextInput(attrs={'class': FROM_INPUT_CLASSES}),
            'description': forms.Textarea(attrs={'class': FROM_INPUT_CLASSES}),
            'price': forms.TextInput(attrs={'class': FROM_INPUT_CLASSES}),
            'image': forms.FileInput(attrs={'class': FROM_INPUT_CLASSES})
        }  
class EditItemform(forms.ModelForm):
    class Meta:
        model=Item
        fields=('name','description','price','image','is_sold')
        widgets={
            'name':forms.TextInput(attrs={'class':FROM_INPUT_CLASSES}),
            'description':forms.Textarea(attrs={'class':FROM_INPUT_CLASSES}),
            'price':forms.TextInput(attrs={'class':FROM_INPUT_CLASSES}),
            'image':forms.FileInput(attrs={'class':FROM_INPUT_CLASSES})
        }