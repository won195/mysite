from django.db import models

# Create your models here.

class Board(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.id}] {self.subject}'

class Comment(models.Model):
    Board = models.ForeignKey(Board, on_delete=models.CASCADE)
    content = models.TextField
    create_date = models.DateTimeField()