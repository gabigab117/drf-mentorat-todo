from rest_framework import serializers
from .models import TodoItem, TodoItemComment

class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = "__all__"


class TodoItemCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = ["title", "description"]
    
    def validate_title(self, value):
        if "patrick" in value.lower():
            raise serializers.ValidationError("On ne touche pas à Patrick")
        return value
