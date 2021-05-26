from django.urls import path
from . import views

app_name = "library"
urlpatterns = [
    path('', views.available_book_list, name="list"),
    path('rented-books/', views.rented_list, name='rented_list'),
    path('<int:book_id>/', views.detail, name="detail"),
    path('<int:book_id>/rented/', views.rent, name='rent'),
    path('<int:book_id>/returned/', views.return_book, name='return'),
    ]
