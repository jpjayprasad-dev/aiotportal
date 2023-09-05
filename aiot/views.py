from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HotelSerializer, FloorSerializer, RoomSerializer, RoomDataSerializer, RoomDataCreateSerializer, RoomControlSerializer, RoomControlCreateSerializer
from .models import Hotel, Room, Floor, Device, DeviceParameter, Data, Control


class HotelItemViews(APIView):
    def get(self, request):
        hotels = Hotel.objects.all()
        serializer = HotelSerializer(hotels, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

class FloorItemViews(APIView):
    def get(self, request, hotel_id):
        rooms = Floor.objects.filter(hotel_id=hotel_id)
        serializer = FloorSerializer(rooms, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

class RoomItemViews(APIView):
    def get(self, request, floor_id):
        rooms = Room.objects.filter(floor_id=floor_id)
        serializer = RoomSerializer(rooms, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

class RoomDataItemViews(APIView):
    def get(self, request, room_id):
        if type == 'data':
            data = Data.objects.filter(room_id=room_id)
            serializer = RoomDataSerializer(data, many=True)
        elif type == 'control':
            control = Control.objects.filter(room_id=room_id)
            serializer = RoomDataSerializer(control, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
 

class RoomDeviceDataItemViews(APIView):
    def get(self, request, room_id, type, device_name):
        device_id = Device.objects.filter(name=device_name).values_list('id', flat=True)[0]
        if type == 'data':
            data = Data.objects.select_related('device_parameter_id').filter(room_id=room_id, device_parameter_id__device_id=device_id)
            serializer = RoomDataSerializer(data, many=True)
        elif type == 'control':
            control = Control.objects.select_related('device_parameter_id').filter(room_id=room_id, device_parameter_id__device_id=device_id)
            serializer = RoomControlSerializer(control, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, room_id, type, device_name):
        device_id = Device.objects.filter(name=device_name).values_list('id', flat=True)[0]
        param = request.data.get('param')
        device_parameter_id = DeviceParameter.objects.filter(device_id=device_id, param=param).values_list('id', flat=True)[0]
        value = request.data.get('value')
        doc = {'device_parameter_id' : device_parameter_id, 'room_id' : int(room_id), 'value' : value}
        if type == 'data':
            serializer = RoomDataCreateSerializer(data=doc)
        elif type == 'control':
            serializer = RoomControlCreateSerializer(data=doc)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


