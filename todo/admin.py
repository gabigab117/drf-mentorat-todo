from django.contrib import admin

from .models import TodoItem, TodoItemComment

admin.site.register(TodoItem)
admin.site.register(TodoItemComment)
