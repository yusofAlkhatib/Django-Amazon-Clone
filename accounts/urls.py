from django.urls import path
from .views import dashboard , signup , user_activate



urlpatterns = [
    path('dashboard',dashboard),
    path('signup' , signup),
    path('<str:username>/activte' , user_activate)
]
