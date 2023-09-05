from django.urls import path
from .views import HotelItemViews, FloorItemViews, RoomItemViews, RoomDataItemViews, RoomDeviceDataItemViews

urlpatterns = [
    path('hotels/', HotelItemViews.as_view()),
    path("hotels/<hotel_id>/floors", FloorItemViews.as_view()),
    path("floors/<floor_id>/rooms", RoomItemViews.as_view()),
    path("rooms/<room_id>/<type>", RoomDataItemViews.as_view()),
    path("rooms/<room_id>/<type>/<device_name>", RoomDeviceDataItemViews.as_view()),
]