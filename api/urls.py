from django.urls import path
from api import views

urlpatterns = [
    # these for api
    path('api/', views.UserForm.as_view()),

    # these for django app
    path('', views.showall, name='list'),
    path('create/', views.user_create, name='create'),
]