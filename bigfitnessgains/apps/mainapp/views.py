from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bigfitnessgains.apps.mainapp import utils
from bigfitnessgains.apps.mainapp.serializers import UserSerializer


def index(request):
    return render(request, 'mainapp/index.html', None)


@api_view(['POST'])
def register(request):
    serialized = UserSerializer(data=request.DATA)
    if serialized.is_valid():
        User.objects.create_user(
            serialized.init_data['email'],
            serialized.init_data['username'],
            serialized.init_data['password'],
            serialized.init_data['first_name'],
            serialized.init_data['last_name']
            )
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST) 