from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    # path('main', views.main, name='main'),
    path('contacts/<str:color>/', views.contacts, name='contacts'),
    path('rooms', views.rooms, name='rooms'),
    # path('<str:color>/', ),
]