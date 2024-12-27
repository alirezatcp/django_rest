from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
def hello(request):
    if request.method == 'GET':
        return Response({'message': 'Hello GET!!!'})

    return Response({'message': "Hello POST!!!"})


# we can use another classes instead of APIView: CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView, GenericAPIView
class GoodBye(APIView):
    # permission_classes = [IsAuthenticated] # if we add this line, user should authenticate to see this page.

    def get(self, request):
        return Response({'message': 'Bye GET!!!'})

    def post(self, request):
        return Response({'message': 'Bye POST!!!'})