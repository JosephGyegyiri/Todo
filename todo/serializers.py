#python object to json object
#converts python object to json object
#converts json object to python object
#converts python object to json string
#converts json string to python object
#converts python object to json file
#converts json file to python object

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

from rest_framework.serializers import ModelSerializer
from .models import Todo

#Get requests
class TodoListSerializer(ModelSerializer):

    class Meta:
        model = Todo
        fields = '__all__' #everything
    