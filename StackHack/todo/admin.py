from django.contrib import admin
from todo.models import(
    Priority,
    Tags,
    Status,
    todo
)

# Register your models here.
admin.site.register(Priority)
admin.site.register(Tags)
admin.site.register(Status)
admin.site.register(todo)