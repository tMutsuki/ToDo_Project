from django.db import models

# Create your models here.
#モデルを継承する
class ToDoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    
    def __str__(self):
        return self.title
    