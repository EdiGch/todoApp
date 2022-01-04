from django.urls import path, include
from . import views

urlpatterns = [
    path('completed/', views.CompletedList.as_view()),
]
