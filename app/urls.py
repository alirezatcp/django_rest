from django.urls import path

from app import views

urlpatterns = [
    path('hello/', views.hello),
    path('bye/', views.GoodBye.as_view()),

    path('add_car/', views.AddCarAPIView.as_view()),
    path('car/<int:car_id>/', views.CarAPIView.as_view()),

    path('hello_api/', views.HelloAPIView.as_view())
]
