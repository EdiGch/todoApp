from django.urls import path, include
from . import views

urlpatterns = [
    path('list-create/', views.ListCreate.as_view()),
    path('<int:pk>', views.RetrieveUpdateDestroy.as_view()),
    path('completed/', views.CompletedList.as_view()),
]
