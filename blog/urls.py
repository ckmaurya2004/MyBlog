
from django.urls import path
from . import views

urlpatterns = [

    path('',views.index,name='home'),
    path('<str:slug>/<int:myid>/',views.blogPost, name = 'blogPost'),
    path('about/<int:pk>',views.about,name = 'about'),
    path('category/<int:myid>',views.category,name = 'category'),
    path('search/',views.search,name = 'search'),
    

]