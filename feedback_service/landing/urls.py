from django.urls import path, URLPattern
from landing import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register),
    path('review/', views.review_view, name="review"),
]
