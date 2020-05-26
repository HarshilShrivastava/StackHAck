from todo.models import(
    todo
)
from rest_framework.response import Response
from rest_framework import status
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
from .serializer import(
    TodoSerializer,
    TodoReadSerializer
)

class Todo(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=(TokenAuthentication,)
    def post(self,request,*args,**kwargs):
        context={}
        data={}
        serializer=TodoSerializer(data=request.data)
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
    def get(self,request,*args,**kwargs):
        context={}
        data={}
        qs=get_list_or_404(todo,User=request.user)
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

