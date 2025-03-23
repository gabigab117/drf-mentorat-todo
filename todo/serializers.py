from rest_framework import serializers
from .models import TodoItem, TodoItemComment


class TodoItemCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoItemComment
        fields = ["todo_item", "comment"]


class TodoItemSerializer(serializers.ModelSerializer):
    comments = TodoItemCommentSerializer(many=True)
    # comments = serializers.StringRelatedField(many=True)

    class Meta:
        model = TodoItem
        fields = ["id", "title", "description", "completed", "created_at", "comments"]
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
    
    def validate(self, data):
        if data["title"] == data["description"]:
            raise serializers.ValidationError("title et description sont identiques voyons !")
        return data
    
    def to_internal_value(self, data):
        # https://docs.djangoproject.com/fr/5.1/ref/request-response/#querydict-objects
        data = data.copy()
        data["title"] = data["title"].upper()
        return super().to_internal_value(data)
    
    def create(self, validated_data): # appelée à la création d'un objet
        todo_item = TodoItem.objects.create(**validated_data)

        # Opérations supplémentaires
        TodoItemComment.objects.create(todo_item=todo_item, comment="Le super commentaire par défaut")
        return todo_item
