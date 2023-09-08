from datetime import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HotelSerializer, FloorSerializer, RoomSerializer, RoomDataSerializer, RoomDataCreateSerializer, RoomControlSerializer, RoomControlCreateSerializer
from .models import Hotel, Room, Floor, Device, DeviceParameter, Data, Control
from psycopg2.extras import DateTimeTZRange
from django.utils import timezone as tz


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

class RoomEntityItemViews(APIView):
    def get(self, request, room_id, type):
        if type == 'data':
            data = Data.objects.filter(room_id=room_id) if room_id != "all" else Data.objects
            print(request.data)
            if request.data.get('timespan'):
                lower_scope = tz.now() - tz.timedelta(seconds=int(request.data.get('timespan')))
                higher_scope = tz.now()
                data = data.filter(timestamp__gte=lower_scope, timestamp__lte=higher_scope)
            serializer = RoomDataSerializer(data, many=True)
        elif type == 'control':
            control = Control.objects.filter(room_id=room_id) if room_id != "all" else Control.objects
            if request.data.get('timespan'):
                lower_scope = tz.now() - tz.timedelta(seconds=int(request.data.get('timespan')))
                higher_scope = tz.now()
                control = control.filter(timestamp__gte=lower_scope, timestamp__lte=higher_scope)
            serializer = RoomDataSerializer(control, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
 

class RoomDeviceEntityItemViews(APIView):
    def get(self, request, room_id, type, device_name):       
        device_id = Device.objects.filter(name=device_name).values_list('id', flat=True)[0]
        if type == 'data':
            data = Data.objects.filter(room_id=room_id) if room_id != "all" else Data.objects
            data = data.select_related('device_parameter_id').filter(device_parameter_id__device_id=device_id)
            print(request.data)
            if request.data.get('timespan'):
                lower_scope = tz.now() - tz.timedelta(seconds=int(request.data.get('timespan')))
                higher_scope = tz.now()
                data = data.filter(timestamp__gte=lower_scope, timestamp__lte=higher_scope)
            serializer = RoomDataSerializer(data, many=True)
        elif type == 'control':
            control = Control.objects.filter(room_id=room_id) if room_id != "all" else Control.objects
            control = control.select_related('device_parameter_id').filter(device_parameter_id__device_id=device_id)
            if request.data.get('timespan'):
                lower_scope = tz.now() - tz.timedelta(seconds=int(request.data.get('timespan')))
                higher_scope = tz.now()
                control = control.filter(timestamp__gte=lower_scope, timestamp__lte=higher_scope)
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


