from django.urls import path
from .views import Index, Detail
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('/post/<int:pk>', Detail.as_view(), name='detail')
]