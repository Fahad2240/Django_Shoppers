from django.urls import path
from .views import details
app_name='item'
urlpatterns=[
    path('items/<int:id>/', details, name='details')
]