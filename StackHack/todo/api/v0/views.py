from todo.models import(
    todo
)


from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend

from django.shortcuts import get_object_or_404,get_list_or_404
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import (
    get_user_model,
)
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets

from .serializer import(
    TodoSerializer,
    TodoReadSerializer,
    SetreminderSerializer
)
from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class TodoListViewset(generics.ListAPIView):
    queryset = todo.objects.all()
    serializer_class = TodoReadSerializer
    http_method_names = ['get']
    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = ['Title','Description']
    filter_fields = ('Status','Color','label',)



    def list(self, request, *args, **kwargs):
        self.object_list=self.filter_queryset(self.get_queryset())
        context={}
        qs=self.object_list
        qs=qs.filter(User=request.user)
        data={}
        serializer=TodoReadSerializer(qs,many=True)
        data=serializer.data
        context['sucess']=True
        context['status']=200
        context['message']="sucessfull get"
        context['count']=qs.count()
        context['data']=data
        return Response(context)


class Todo(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=(TokenAuthentication,)
    
    def post(self,request,*args,**kwargs):
        context={}
        data={}
        serializer=TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(User=request.user,Is_Archeived=False)
            context['status']=200
            context['sucess']=True
            context['message']="sucessfully created"
            data=serializer.data
            context['data']=data
            return Response(context)
        else:
            context['status']=400
            context['sucess']=False
            context['message']="not  created"
            data=serializer.errors
            context['data']=data
            return Response(context)
    def get(self,request,*args,**kwargs):
        context={}
        data={}
        qs=todo.objects.filter(User=request.user)
        qs=qs.filter(Is_Archeived=False)
        serializer=TodoReadSerializer(qs,many=True)
        context['status']=200
        context['sucess']=True
        context['message']="sucessfully created"
        data=serializer.data
        context['data']=data
        return Response(context)


class Tododetail(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=(TokenAuthentication,)
    def put(self,request,id,*args,**kwargs):
        context={}
        data={}
        try:
            obj=get_object_or_404(todo,pk=id)
        except:
            context['sucess']=False
            context['status']=400
            context['message']="can't update"
            context['data']=data
            return Response(context)
        serializer=TodoSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save(User=request.user)
            context['status']=200
            context['sucess']=True
            context['message']="sucessfully created"
            data=serializer.data
            context['data']=data
            return Response(context)
        else:
            context['status']=400
            context['sucess']=False
            context['message']="not  created"
            data=serializer.errors
            context['data']=data
            return Response(context)
    def delete(self,request,id,*args,**kwargs):
        context={}
        data={}
        try:
            qs=get_object_or_404(todo,pk=id)
            obj=qs.delete()
        except:
            context['status']=400
            context['sucess']=False
            context['message']="not  found"
            data=serializer.errors
            context['data']=data
            return Response(context)
        context['status']=200
        context['sucess']=True
        context['message']="sucessfully deleted"
        context['data']=data
        return Response(context)
@api_view(('PUT',))
@permission_classes((IsAuthenticated,))
def update(request,id):
    context={}
    data={}
    try:
        obj=get_object_or_404(todo,pk=id)
    except:
        context['status']=400
        context['sucess']=False
        context['message']="not  found"
        context['data']=data
        return Response(context)
    serializer=SetreminderSerializer(data=request.data)
    if serializer.is_valid():
        obj.Remind=serializer.validated_data['Remind']
        obj.save()
        context['status']=200
        context['sucess']=True
        context['message']="sucessfully updated"
        context['data']=data
        return Response(context)
    else:
        context['status']=400
        context['sucess']=False
        context['message']="Wrong format"
        context['data']=data
        return Response(context)

@api_view(['PUT', ])
@permission_classes((AllowAny, ))
def Put_in_Archeieve(request,id):
    data={}
    context={}
    try:
        obj=get_object_or_404(todo,pk=id)
    except:
        context['status']=400
        context['sucess']=False
        context['message']="not  found"
        context['data']=data
        return Response(context)
    obj.Is_Archeived=True
    obj.save()
    context['status']=200
    context['sucess']=True
    context['message']="sucessfully updated"
    context['data']=data
    return Response(context)



@api_view(['GET', ])
@permission_classes((IsAuthenticated, ))
def ArcheieveList(request):
    data={}
    context={}
    qs=todo.objects.filter(Is_Archeived=True).filter(User=request.user)
    serializer=TodoReadSerializer(qs,many=True)
    context['status']=200
    context['sucess']=True
    context['message']="sucessfully created"
    data=serializer.data
    context['data']=data
    return Response(context)


@api_view(['PUT', ])
@permission_classes((AllowAny, ))
def remove_from_archeieve(request,id):
    data={}
    context={}
    try:
        obj=get_object_or_404(todo,pk=id)
    except:
        context['status']=400
        context['sucess']=False
        context['message']="not  found"
        context['data']=data
        return Response(context)
    obj.Is_Archeived=False
    obj.save()
    context['status']=200
    context['sucess']=True
    context['message']="sucessfully removed"
    context['data']=data
    return Response(context)