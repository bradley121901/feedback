from django.urls import path, URLPattern
from landing import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register),
]
