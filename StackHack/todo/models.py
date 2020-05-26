from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class Priority(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Tags(models.Model):
    Color=models.CharField(max_length=50)
    def __str__(self):
        return self.Color

class Status(models.Model):
    label=models.CharField(max_length=50)
    def __str__(self):
        return self.label


class todo(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.CharField(max_length=50)
    Description=models.TextField()
    Created_at=models.DateTimeField(auto_now_add=True)
    Remind=models.DateTimeField(null=True,blank=True)
    Status = models.ForeignKey(Status, on_delete=models.CASCADE)
    Color = models.ForeignKey(Tags, on_delete=models.CASCADE)
    Priority = models.ForeignKey(Priority, on_delete=models.CASCADE,null=True,blank=True)



