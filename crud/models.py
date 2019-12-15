from django.db import models

# Create your models here.
class Todo(models.Model):
    task_desc = models.CharField(max_length=200)
    def __str__(self):
        return self.task_desc