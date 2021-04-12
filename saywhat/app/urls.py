from django.urls import path
from .views import Index, Detail, newpost, register
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('post/<int:pk>', Detail.as_view(), name='detail'),
    path("newpost", newpost, name='newpost'),
    path("register", register, name='register')
]