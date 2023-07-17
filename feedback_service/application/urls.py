from django.urls import path, URLPattern
from application import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', views.index, name="index"),
    path('addproduct/', views.product_page),
    path('review/', views.review_page),
]
