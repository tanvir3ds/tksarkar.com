from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.home, name= 'home'),
    path('profile', views.profile, name= 'profile'),
    path('awards', views.awards, name= 'awards'),
    path('interviews', views.interviews, name= 'interviews'),
    path('photos', views.photos, name= 'photos'),
    path('blog', views.blog, name= 'blog'),


    
    
  
]
