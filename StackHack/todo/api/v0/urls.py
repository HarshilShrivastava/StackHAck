from django.urls import path
from .views import Todo,Tododetail,update
urlpatterns = [
    path('todo/',Todo.as_view(),name="post and get"),
    path('tododetail/<int:id>',Tododetail.as_view(),name="post and get"),
    path('update/<int:id>',update,name="update reminder date"),
]
