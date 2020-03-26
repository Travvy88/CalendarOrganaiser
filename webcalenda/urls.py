from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_calendar, name='show_calendar'),
    path('<int:y>/<int:m>/', views.show_month, name='show_month'),
]