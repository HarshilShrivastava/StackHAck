from django.urls import path
from .views import Todo,Tododetail,update,Put_in_Archeieve,ArcheieveList,TodoListViewset
urlpatterns = [
    path('todo/',Todo.as_view(),name="post and get"),
    path('tododetail/<int:id>',Tododetail.as_view(),name="post and get"),
    path('filter/',TodoListViewset.as_view(),name="high bt"),
    path('update/<int:id>',update,name="update reminder date"),
    path('Archeive/<int:id>',Put_in_Archeieve,name="put in archeive"),
    path('ArcheiveList/',ArcheieveList,name="list of archeive todo"),
]
