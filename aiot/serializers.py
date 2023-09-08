from rest_framework import serializers
from .models import Hotel, Room, Floor, Device, DeviceParameter, Data, Control

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'name']

class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = ['id', 'number']

class RoomSerializer(serializers.ModelSerializer):
     class Meta:
        model = Room
        fields = ['id', 'number']

class DeviceSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Device
        fields = ['id', 'name']

class DeviceParameterSerializer(serializers.HyperlinkedModelSerializer):
     device_id = DeviceSerializer()
     class Meta:
        model = DeviceParameter
        fields = ['id', 'device_id', 'param']

class RoomDataSerializer(serializers.HyperlinkedModelSerializer):
     device_parameter_id = DeviceParameterSerializer()
     room_id = RoomSerializer()
     class Meta:
        model = Data
        fields = ( 'device_parameter_id', 'value', 'timestamp', 'room_id')

class RoomDataCreateSerializer(serializers.ModelSerializer):
     class Meta:
        model = Data
        fields = ( 'device_parameter_id', 'value', 'room_id')

class RoomControlSerializer(serializers.HyperlinkedModelSerializer):
     device_parameter_id = DeviceParameterSerializer()
     room_id = RoomSerializer()
     class Meta:
        model = Control
        fields = ( 'device_parameter_id', 'value', 'timestamp', 'room_id')

class RoomControlCreateSerializer(serializers.ModelSerializer):
     class Meta:
        model = Control
        fields = ( 'device_parameter_id', 'value', 'room_id')
