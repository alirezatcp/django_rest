from rest_framework.generics import CreateAPIView

from about_signals.serializers import ProductSerializer


class ProductAPIView(CreateAPIView):
    serializer_class = ProductSerializer
    
