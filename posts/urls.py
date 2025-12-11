from django.urls import path
from .views import post_list, post_detail, post_create, post_update, post_delete

app_name = 'posts'

urlpatterns = [
    path('', post_list, name='list'),
    path('post/new/', post_create, name='create'),
    path('post/<int:pk>/', post_detail, name='detail'),
    path('post/<int:pk>/edit/', post_update, name='update'),
    path('post/<int:pk>/delete/', post_delete, name='delete'),
]
