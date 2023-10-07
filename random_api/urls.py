from django.urls import path
from . import views

urlpatterns = [
    path('random/', views.random_data, name='random_data'),
]
