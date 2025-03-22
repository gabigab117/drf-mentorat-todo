from rest_framework import serializers
from .models import TodoItem, TodoItemComment


class TodoItemCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoItemComment
        fields = ["todo_item", "comment"]


class TodoItemSerializer(serializers.ModelSerializer):
    comments = TodoItemCommentSerializer(many=True)

    class Meta:
        model = TodoItem
        fields = ["title", "description", "completed", "created_at", "comments"]
        # depth = 1
    
    def to_representation(self, instance):
        todo_repr = super().to_representation(instance)
        todo_repr["comments_number"] = instance.comments.count()
        if instance.completed:
            todo_repr["completed"] = "Terminé !"
        return todo_repr


class TodoItemCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoItem
        fields = ["title", "description"]
    
    def validate_title(self, value):
        if "patrick" in value.lower():
            raise serializers.ValidationError("On ne touche pas à Patrick")
        return value
