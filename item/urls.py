from django.urls import path
from . import views
app_name='item'
urlpatterns=[
    path('add/',views.add_new,name='add'),
    path('items/<int:pk>/',views.details, name='details')
]