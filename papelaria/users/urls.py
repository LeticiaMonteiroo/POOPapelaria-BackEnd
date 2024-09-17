from django.urls import path
from . import views

urlpatterns = [
    # path('cadastro/', views.cadastro_api),
    path('login/', views.login_api)
]