from .views import login,register,user_logout,Blog_list
from django.urls import path
from . import views


urlpatterns = [
    path('login/',login,name='login'),
    path('register/',register,name='register'),
    path('logout/',user_logout,name='logout'),
    path('Blog_list/',Blog_list,name='Blog_list'),
    path('Blog_list/create_blog/', views.create_blog,name='create_blog'),
    path('Blog_list/<int:blog_id>/edit/', views.edit_blog,name='edit_blog'),
    path('Blog_list/<int:blog_id>/delete/',views.delete_blog,name='delete_blog')
]
