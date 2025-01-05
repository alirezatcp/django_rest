from rest_framework.generics import CreateAPIView

from about_signals.serializers import ProductSerializer

# using logger (default showing more than debug logs)
import logging

logger = logging.getLogger(__name__)

class ProductAPIView(CreateAPIView):
    logger.warning('This is a warning!!!!')
    logger.critical('This is a critical!!!')
    
    serializer_class = ProductSerializer
    
