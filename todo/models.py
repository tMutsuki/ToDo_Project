from django.db import models

# Create your models here.
#モデルを継承する

CHOICE = (('danger', 'high'), ('warning', 'normal'), ('primary', 'low'))

#★★★★★★★★★★★★★★★★★★
#クラス: 実際に作成するもの
#★★★★★★★★★★★★★★★★★★  
class ToDoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(max_length = 50,
                                choices = CHOICE,
                                null=True
                                )
    duedate = models.DateField()
    
    def __str__(self):
        return self.title
    