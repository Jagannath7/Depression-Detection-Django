from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('about', views.about, name="about"),
    path('data', views.data, name='data'),
    path('myaccount', views.myaccount, name='myaccount'),
    path('edit', views.edit, name='edit'),
    path('passwordreset', views.passwordReset, name='passwordreset')
]