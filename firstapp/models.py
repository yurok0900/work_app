from django.db import models

class TaskModel(models.Model):
    name = models.CharField(max_length = 150)
    text_template = models.ForeignKey('TextModel', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class TextModel(models.Model):
    text = models.CharField(max_length=100)
    
    def __str__(self):
        return self.text