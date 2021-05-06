from .models import TaskModel, TextModel
from django.forms import ModelForm


class TaskForm(ModelForm):
    
    class Meta:
        model = TaskModel
        fields = ('name','text_template')

class TextForm(ModelForm):
    
    class Meta:
        model = TextModel
        fields = ('text',)