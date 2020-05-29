from rest_framework import serializers
from todo.models import(
    todo
)
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=todo
        exclude=('User','Created_at','Is_Archeived')

class TodoReadSerializer(serializers.ModelSerializer):
    Status=serializers.SerializerMethodField('get_Status')
    Color=serializers.SerializerMethodField('get_color')
    label=serializers.SerializerMethodField('get_label')
    class Meta:
        model=todo
 #       fields='__all__'
        fields=['id','Title','Description','Created_at','Remind','DueDate','Status','Color','label']
    def get_Status(self,info):
        Data=info.Status.label
        return Data
    def get_color(self,info):
        Data=info.Color.Color
        return Data
    def get_label(self,info):
        Data=info.label.name
        return Data

class SetreminderSerializer(serializers.ModelSerializer):
    class Meta:
        model=todo
        fields=['Remind']