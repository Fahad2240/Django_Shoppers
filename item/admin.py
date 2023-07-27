from django.contrib import admin

from item.models import Item, category

# Register your models here.
admin.site.register(category)
admin.site.register(Item)