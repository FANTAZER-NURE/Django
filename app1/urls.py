from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('', views.main, name='main'),
    path('contacts/<str:color>/', views.contacts, name='contacts'),
    path('rooms', views.rooms, name='rooms'),
    path('accounts/login/', LoginView.as_view(), name='login'),

    path('accounts/login/', LoginView.as_view(), name='login'),

    path('book', views.book, name='book'),
]