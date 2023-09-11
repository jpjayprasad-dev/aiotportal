# AIOT PORTAL
The python DJango app syncs the sensor/devices data/control with the persistent DB hosted in postgres via API calls.

## Setup

1. Install docker
2. Clone this git repo.
```
git clone https://github.com/jpjayprasad-dev/aiotportal/ .
```

## Build Image
```
docker build -t aiotportal:latest .
```

## Application Specs

The following environment variables determines the running configuration of the portal
```
POSTGRES_HOST = The ip addrerss of the host where the postgres DB running.
POSTGRES_PORT = The port where the postgres DB is running.
POSTGRES_DB = The name of the postgres DB in which the sensor/device data/control points will be stored.
POSTGRES_USER = Username to access postgres DB 
POSTGRES_PASSWORD = Password to access postgres DB
```

## Run Service
```
docker run --rm -d -p 8800:8800 -e POSTGRES_HOST=<postgres_host> -e POSTGRES_PORT=<postgres_port> -e POSTGRES_DB=<postgres_db> -e POSTGRES_USER=<postgres_user> -e POSTGRES_PASSWORD=<postgres_password> --name aiot-portal aiotportal:latest

```

## USAGES
1. Go to the browser http://<host_ip>:8800/admin to access the DB administration via DJango app.
2. The service provides the below APIs to fetch IoT sensor data and post IoT controls.
   ```
   a. [url](http://<host_ip>:8800)/hotels/: Retrieve all hotels.
   b. [url](http://<host_ip>:8800)/hotels/<hotel_id>/floors/: Access floors in a hotel.
   c. [url](http://<host_ip>:8800)/floors/<floor_id>/rooms/: List rooms on a floor.
   d. [url](http://<host_ip>:8800)/rooms/<room_id>/data/: Get IoT data for a room.
   e. [url](http://<host_ip>:8800)/rooms/<room_id>/data/life_being/: Life Being sensor data.
   f. [url](http://<host_ip>:8800)/rooms/<room_id>/data/iaq/: IAQ sensor data.
   g. [url](http://<host_ip>:8800)/rooms/<room_id>/control/aircon/: Device control data. POST with a payload structure '{"param":<control_paramenter>, "value":<control_value>}'
   ```

## Examples [Screenshots]
To get life_being sensor data from a room with id 3
<img width="1504" alt="image" src="https://github.com/jpjayprasad-dev/aiotportal/assets/73153441/f7dade52-bdd6-4fea-9a45-3a517eb76a8f">


To post aircon device control temperature to the room with id 3
<img width="1504" alt="image" src="https://github.com/jpjayprasad-dev/aiotportal/assets/73153441/c20441aa-2dfe-485d-a1ac-9260a5b31f39">
