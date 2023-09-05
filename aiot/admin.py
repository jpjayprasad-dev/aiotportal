from django.contrib import admin
from .models import Hotel, Floor, Room, Data, Control, Device, DeviceParameter

admin.site.register(Hotel)
admin.site.register(Floor)
admin.site.register(Room)
admin.site.register(Device)
admin.site.register(DeviceParameter)
admin.site.register(Data)
admin.site.register(Control)
