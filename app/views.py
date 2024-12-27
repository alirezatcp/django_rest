from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import get_object_or_404

from app.serializers import CarSerializer
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
        car_serializer = CarSerializer(data=request.data)
        if car_serializer.is_valid():
            car_serializer.save()
            return Response({'message': 'Car added successfully.'})

        return Response({'message': car_serializer.errors})


class CarAPIView(APIView):
    def get(self, request, car_id):
        car = get_object_or_404(Car, id=car_id)
        car_serializer = CarSerializer(instance=car)
        data = car_serializer.data
        return Response({'car': data})

    def put(self, request, car_id):
        car = get_object_or_404(Car, id=car_id)
        car_serializer = CarSerializer(instance=car, data=request.data, partial=True) # partial=True is for that user can update partial of model too.
        if car_serializer.is_valid():
            car_serializer.save()
            return Response({'message': 'Car updated successfully!'})

        return Response({'message': car_serializer.errors})
