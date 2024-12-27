from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404, GenericAPIView

from app.serializers import CarSerializer, CarModelSerializer
from app.models import Car

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


class AddCarAPIView(APIView):
    def post(self, request):
        car_serializer = CarModelSerializer(data=request.data)
        if car_serializer.is_valid():
            car_serializer.save()
            return Response({'message': 'Car added successfully.'})

        return Response({'message': car_serializer.errors})


class CarAPIView(APIView):
    def get(self, request, car_id):
        car = get_object_or_404(Car, id=car_id)
        car_serializer = CarModelSerializer(instance=car)
        data = car_serializer.data
        return Response({'car': data})

    def put(self, request, car_id):
        car = get_object_or_404(Car, id=car_id)
        car_serializer = CarModelSerializer(instance=car, data=request.data, partial=True) # partial=True is for that user can update partial of model too.
        if car_serializer.is_valid():
            car_serializer.save()
            return Response({'message': 'Car updated successfully!'})

        return Response({'message': car_serializer.errors})


# to access this view we should login first and request our username and password with post to login/ and get the token and replace token as header of this view.
# key = Authorization 
# value = Token {token_we_got}
class HelloAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response({'message': f'Hello {request.user.username}!'})


class LogoutAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        request.user.auth_token.delete()
        return Response({'message': f'Bye {request.user.username}!'})