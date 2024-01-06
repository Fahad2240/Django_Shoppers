from django.urls import path
from . import views
app_name='item'
urlpatterns=[
    path('items/',views.items,name='items'),
    path('add/',views.add_new,name='add'),
    path('items/<int:pk>/',views.details, name='details'),
    path('<int:pk>/delete/',views.delete,name='delete'),
    path('<int:pk>/edit/',views.edit,name='edit')
]