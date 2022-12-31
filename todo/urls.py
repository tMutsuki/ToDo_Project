from django.urls import path, include
from .views import ToDoList, ToDoDetail

urlpatterns = [
    path('list/', ToDoList.as_view()),
    path('detail/<int:pk>', ToDoDetail.as_view())
]