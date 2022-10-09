from django.urls import path
from .views import DroneListAPIView, DroneCreateAPIView, LoadDroneAPIView

urlpatterns = [
    path('all/', DroneListAPIView.as_view(), name='drones'),
    path('register/', DroneCreateAPIView.as_view(), name='register_drone'),
    path('<int:pk>/add_medications/', LoadDroneAPIView.as_view(), name='add_medications'),
    
]