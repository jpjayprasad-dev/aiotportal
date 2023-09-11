from django.urls import path
from .views import HotelItemViews, HotelViews, FloorItemViews, RoomItemViews, RoomEntityItemViews, RoomDeviceEntityItemViews

urlpatterns = [
    path('hotels/', HotelItemViews.as_view()),
    path('hotels/<name>', HotelViews.as_view()),
    path("hotels/<hotel_id>/floors", FloorItemViews.as_view()),
    path("floors/<floor_id>/rooms", RoomItemViews.as_view()),
    path("rooms/<room_id>/<type>", RoomEntityItemViews.as_view()),
    path("rooms/<room_id>/<type>/<device_name>", RoomDeviceEntityItemViews.as_view()),
]