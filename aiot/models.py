from django.db import models

class Hotel(models.Model):

    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Floor(models.Model):

    id = models.AutoField(primary_key=True)

    number = models.CharField(max_length=20)

    hotel_id = models.ForeignKey("Hotel", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.number

class Room(models.Model):

    id = models.AutoField(primary_key=True)

    number = models.CharField(max_length=20)

    floor_id = models.ForeignKey("Floor", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.number

class Device(models.Model):

    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class DeviceParameter(models.Model):

    id = models.AutoField(primary_key=True)

    param = models.CharField(max_length=40)

    device_id = models.ForeignKey("Device", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.param

class Data(models.Model):

    device_parameter_id = models.ForeignKey("DeviceParameter", on_delete=models.SET_NULL, null=True)

    value = models.CharField(max_length=200)

    timestamp = models.DateTimeField(auto_now_add=True)

    room_id = models.ForeignKey("Room", on_delete=models.SET_NULL, null=True)

class Control(models.Model):

    device_parameter_id = models.ForeignKey("DeviceParameter", on_delete=models.SET_NULL, null=True)

    value = models.CharField(max_length=200)

    timestamp = models.DateTimeField(auto_now_add=True)

    room_id = models.ForeignKey("Room", on_delete=models.SET_NULL, null=True)

