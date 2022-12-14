
from itertools import count
from django.shortcuts import render
from .models import Drone, Medication
from rest_framework.viewsets import GenericViewSet 
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import DroneSerializer, DroneCreateSerializer, DroneUpdateSerializer, \
    DroneMedicationsItemsSerializer, DroneBasicSerializer, DroneBatterySerializer, MediacationSerializer\
    ,DroneHistorySerializer, MediacationBasicSerializer    
# Create your views here.


class DroneListAPIView(generics.ListAPIView):
    serializer_class = DroneSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()

class DroneCreateAPIView(generics.CreateAPIView):
    serializer_class = DroneCreateSerializer

    def create(self, request):
        if not str(request.data['serial_number']).isalnum():
            return Response({'error':'This field only allows alpha-numeric characters.'}, status=status.HTTP_400_BAD_REQUEST)

        if len(str(request.data['serial_number'])) > 100:
            return Response({'message':'The number of characters for this field must be less than 100.'}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Drone successfully created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoadDroneAPIView(generics.UpdateAPIView):
    serializer_class = DroneUpdateSerializer

    def get_queryset(self,pk):
        return self.get_serializer().Meta.model.objects.filter(state = '1').filter(id = pk).first()


    def patch(self, request, pk=None):
        cont=0
        datas = str(request.data)[1:-2].split(":")
        datas = datas[1].strip()
        
        for id in datas:
           if id.isdigit():
            medication = Medication.objects.get(id = int(id))
            cont+=medication.weight
        drone = Drone.objects.get(id = pk)
        
        if cont > drone.weight_limit:
            return Response({'error':'The weight of all medications exceeds the weight limit of this drone.'}, status = status.HTTP_400_BAD_REQUEST)
        
        if drone.battery_level < 25 :
            return Response({'error':'Ups... Drone with insufficient battery. It will be ready in a while.'}, status = status.HTTP_400_BAD_REQUEST)

        elif self.get_queryset(pk):
            drone_serializer = self.serializer_class(self.get_queryset(pk), data= request.data)

            if drone_serializer.is_valid():
                drone_serializer.save()
                return Response(drone_serializer.data, status = status.HTTP_200_OK)
            return Response(drone_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        return Response({'error':'This drone does not exist'}, status = status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk=None):
        print(request.data)
        cont=0
        datas = str(request.data)[1:-2].split(":")
        datas = datas[2].strip()
        
        for id in datas:
           if id.isdigit():
            medication = Medication.objects.get(id = int(id))
            cont+=medication.weight

        drone = Drone.objects.get(id = pk)
        

        if cont > drone.weight_limit:
            return Response({'error':'The weight of all medications exceeds the weight limit of this drone.'}, status = status.HTTP_400_BAD_REQUEST)
        

        if drone.battery_level < 25 :
            return Response({'error':'Ups... Drone with insufficient battery. It will be ready in a while.'}, status = status.HTTP_400_BAD_REQUEST)

        elif self.get_queryset(pk):
            drone_serializer = self.serializer_class(self.get_queryset(pk), data= request.data)

            if drone_serializer.is_valid():
                drone_serializer.save()
                return Response(drone_serializer.data, status = status.HTTP_200_OK)
            return Response(drone_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        return Response({'error':'This drone does not exist'}, status = status.HTTP_400_BAD_REQUEST)
        
class CheckItemsDroneAPIView(generics.RetrieveAPIView):
    serializer_class = DroneMedicationsItemsSerializer

    def get_queryset(self,pk):
        return self.get_serializer().Meta.model.objects.filter(id = pk).first()
            
    def get(self, request, pk=None):
        if self.get_queryset(pk).medications.count() == 0:
            return Response({'error':'This Drone does not have any medical items.'}, status = status.HTTP_400_BAD_REQUEST)

        elif self.get_queryset(pk):
            drone_serializer = self.serializer_class(self.get_queryset(pk))
            return Response(drone_serializer.data, status = status.HTTP_200_OK)
        return Response({'error':'This drone does not exist'}, status = status.HTTP_400_BAD_REQUEST)

class DroneListAvailableAPIView(generics.ListAPIView):
    serializer_class = DroneBasicSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(battery_level__gte=25.0).filter(state = 1)

class CheckBaterryAPIView(generics.RetrieveAPIView):
    serializer_class = DroneBatterySerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()

class MedicationCreateAPIView(generics.CreateAPIView):
    serializer_class = MediacationBasicSerializer

    def create(self, request):
        
        for element in str(request.data['name']):
            if not element.isalnum() and not element=='-' and not element=='_':
                return Response({'error':'The "name" field allows only alphanumeric characters, "-" or "_".'}, status=status.HTTP_400_BAD_REQUEST)
        

        if str(request.data['code']).isupper():
            for element in str(request.data['code']):
                
                if not element.isalnum() and not element=='_':
                    return Response({'error':'The "code" field allows only uppercase letters, underscores and numbers.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error':'The "code" field allows only uppercase letters, underscores and numbers.'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not str(request.data['weight']).isnumeric:
            return Response({'error':'The "weight" field allows only numbers.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Medication successfully created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MedicationListAPIView(generics.ListAPIView):
    serializer_class=MediacationSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()

class DroneHistoryListAPIView(generics.ListAPIView):
    serializer_class=DroneHistorySerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.all()