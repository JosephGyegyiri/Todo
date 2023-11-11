from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import TodoListSerializer
from .models import Todo
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework import permissions
# Create your views here.
#CRUD
#Create, Read, Update, Delete




class TodoListViewSet(ModelViewSet):
    serializer_class = TodoListSerializer
    queryset = Todo.objects.all()
    permission_classes = [permissions.AllowAny] #or use [permissions.IsAuthenticated]
'''''''''
    def list(self, request):
        todo_list = self.get_queryset()
        serialized_todo_list = self.serializer_class(todo_list, many=True)
        return Response(data={
            "message": "Todo list data fetched successfully",
            "data": serialized_todo_list.data
            },status=HTTP_200_OK)
    #permission_classes = [permissions.IsAuthenticated]

    def list (self, request):
        todo_list = self.get_queryset()
        serialized_todo_list = self.get_serializer(todo_list, many=True)

        return Response(data ={
            "message": "Todo list data fetched successfully",
            "data":serialized_todo_list.data
            }, status=HTTP_200_OK)

            '''''''''
