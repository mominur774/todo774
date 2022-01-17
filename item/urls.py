from django.urls import path
from . import views

urlpatterns = [
    path('', views.addPlanView, name='home'),
    path('update/<str:slug>/', views.updatePlanView, name='update'),
    path('delete/<int:pk>/', views.deletePlanView, name='delete'),
]
