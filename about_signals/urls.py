from django.urls import path

from about_signals.views import ProductAPIView

urlpatterns = [
    path('product_signal/', ProductAPIView.as_view())
]