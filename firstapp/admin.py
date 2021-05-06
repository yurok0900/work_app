from django.contrib import admin
from firstapp.models import TaskModel, TextModel

admin.site.register(TaskModel)
admin.site.register(TextModel)