from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import ToDoModel
from django.urls import reverse_lazy

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
    
#★★★★★★★★★★★★★★★★★★
#クラス: 詳細を表示するためのクラス
#★★★★★★★★★★★★★★★★★★
class ToDoCreate(CreateView):
    template_name = "create.html"
    model = ToDoModel
    fields = ('title', "memo", "priority", "duedate")
    success_url = reverse_lazy('list')
    
#★★★★★★★★★★★★★★★★★★
#クラス: リストを削除する
#★★★★★★★★★★★★★★★★★★
class ToDoDelete(DeleteView):
    template_name = "delete.html"
    model = ToDoModel
    success_url = reverse_lazy("list")
  
#★★★★★★★★★★★★★★★★★★
#クラス: リストを更新する
#★★★★★★★★★★★★★★★★★★  
class ToDoUpdate(UpdateView):
    template_name = "update.html"
    model = ToDoModel
    fields = ('title', "memo", "priority", "duedate")
    success_url = reverse_lazy("list")