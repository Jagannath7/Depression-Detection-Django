from django.urls import path
from . import views

urlpatterns = [
    path('books',views.book, name='book'),
    path('videos',views.video, name='video'),
    path('movies',views.movie, name='movie'),
   
]