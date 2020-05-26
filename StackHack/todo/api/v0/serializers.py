from rest_framework import serializers
from todo.models import(
    todo
)
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=todo
        fields=['Title','Description','Created_at','']
