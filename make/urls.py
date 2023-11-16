from django.contrib.auth import views as auth_view
from django.urls import path
from .import views
# from .forms import SignupForm

app_name='make'
urlpatterns=[
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('contact/',views.contact,name='contact')
]