from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('add_book/', add_book, name='add_book'),
    path('book/<int:pk>', book, name='book'),
    path('issue_book/<int:pk>', issue_book, name='issue_book'),
    path('return_book/<int:pk>', return_book, name='return_book'),
    path('delete_book/<int:pk>', delete_book, name='delete_book'),
    path('update_book/<int:pk>', update_book, name='update_book'),
]