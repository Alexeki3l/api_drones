from django.urls import path
from .views import DroneListAPIView, DroneCreateAPIView, LoadDroneAPIView, CheckItemsDroneAPIView, DroneListAvailableAPIView, CheckBaterryAPIView\
    ,MedicationCreateAPIView, MedicationListAPIView, DroneHistoryListAPIView
    
app_name = 'drone'

urlpatterns = [
    path('drones/', DroneListAPIView.as_view(), name='drones'),
    path('dron_register/', DroneCreateAPIView.as_view(), name='register_drone'),
    path('add_medications_drone/<int:pk>', LoadDroneAPIView.as_view(), name='add_medications'),

    path('check_items_drone/<int:pk>', CheckItemsDroneAPIView.as_view(), name='check_items'),
    path('drones_available/', DroneListAvailableAPIView.as_view(), name='drones_available'),
    path('drone_check_baterry/<int:pk>', CheckBaterryAPIView.as_view(), name='drone_check_baterry'),

    path('create_medication/', MedicationCreateAPIView.as_view(), name='create_medication'),
    path('medications/', MedicationListAPIView.as_view(), name='medications'),

    path('drones/log', DroneHistoryListAPIView.as_view(), name='drones_log'),
]