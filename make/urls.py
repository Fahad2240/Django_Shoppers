from django.contrib.auth import views as auth_view
from django.urls import path
from .import views
# from .forms import SignupForm
from .forms import LoginForm

app_name='make'
urlpatterns=[
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html',
         authentication_form=LoginForm), name='login'),
    path('contact/',views.contact,name='contact')
]