from rest_framework import serializers,status
from .models import Drone, Medication
from .utils import change_state
import threading


class MediacationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = ('name', 'weight','code', 'image',)

class DroneSerializer(serializers.ModelSerializer):
    # medications = MediacationSerializer(many=True, read_only=True)
    
    class Meta:
        model = Drone
        fields = ('serial_number', 'model','state','weight_limit','medications',)
    
    def to_representation(self, instance):
        queryset = instance.medications.all()
        serializer = MediacationSerializer(queryset, many=True)
        
        return {
            'id':instance.id,
            'serial_number':instance.serial_number,
            'model':instance.get_model_display(),
            'state':instance.get_state_display(),
            'weight_limit':instance.weight_limit,
            'battery_level':instance.battery_level,
            'medications':serializer.data
        }

class DroneCreateSerializer(serializers.ModelSerializer):
    # medications = MediacationSerializer(many=True, read_only=True)
    
    class Meta:
        model = Drone
        fields = ('serial_number', 'model',)

    def create(self, validated_data):
        print(validated_data)
        return super().create(validated_data)

class DroneUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Drone
        fields = ('medications',)

    def to_representation(self, instance):
        queryset = instance.medications.all()
        serializer = MediacationSerializer(queryset, many=True)
        
        return {
            
            'medications':serializer.data
        }

    def update(self, instance, validated_data):
        if instance.state == '1':
            t = threading.Thread(target=change_state, args=(instance,))
            t.start()
        return super().update(instance, validated_data)

class DroneMedicationsItemsSerializer(serializers.ModelSerializer):
    # medications = MediacationSerializer(many=True, read_only=True)
    
    class Meta:
        model = Drone
        fields = ('serial_number', 'medications',)
    
    def to_representation(self, instance):
        queryset = instance.medications.all()
        serializer = MediacationSerializer(queryset, many=True)
        
        return {
            'id':instance.id,
            'serial_number':instance.serial_number,
            'medications':serializer.data
        }
    
class DroneBasicSerializer(serializers.ModelSerializer):
    # medications = MediacationSerializer(many=True, read_only=True)
    
    class Meta:
        model = Drone
        fields = ('serial_number', 'model','state','weight_limit', 'battery_level')

    def to_representation(self, instance):
        
        return {
            
            'serial_number':instance.serial_number,
            'model':instance.get_model_display(),
            'state':instance.get_state_display(),
            'weight_limit':instance.weight_limit,
            'battery_level':instance.battery_level,
            
        }

class DroneBatterySerializer(serializers.ModelSerializer):
    class Meta:
        model = Drone
        fields = ('battery_level',)

    def to_representation(self, instance):
        
        return {
            'serial_number':instance.serial_number,
            'battery_level':instance.battery_level,
        }