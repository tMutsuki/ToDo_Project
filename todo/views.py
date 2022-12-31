from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import ToDoModel

# Create your views here.
#★★★★★★★★★★★★★★★★★★
#クラス: 一覧で表示するためのクラス
#★★★★★★★★★★★★★★★★★★
class ToDoList(ListView):
    template_name = "list.html"
    model = ToDoModel
    
#★★★★★★★★★★★★★★★★★★
#クラス: 詳細を表示するためのクラス
#★★★★★★★★★★★★★★★★★★
class ToDoDetail(DetailView):
    template_name = "detail.html"
    model = ToDoModel