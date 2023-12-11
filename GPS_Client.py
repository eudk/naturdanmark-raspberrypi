from socket import *
import json
import time
import requests


servername='255.255.255.255'
serverport=12000
clientsocket= socket(AF_INET,SOCK_DGRAM)
clientsocket.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

baseurl="https://naturdanmark-api20231124193012.azurewebsites.net/Api/Observation"
Observations=requests.get(baseurl).content
Observations=json.loads(Observations)

def sending(data):
    print("sending")
    Koordinates={"deviceID": id,"longitude":longitudes,'Latitude':lattitudes,"date": "2023-12-06T13:38:33.874Z"}
    clientsocket.sendto(json.dumps(Koordinates).encode(),(servername,serverport))

id=0
while True:
    for obs in Observations:
        longitudes=obs['longitude']
        lattitudes=obs['latitude']
        sending("hello")
        if(id==0):
            Koordinates,serverAddress=clientsocket.recvfrom(1024)
            Koordinates=Koordinates.decode()
            print('message received')
            Koordinates=json.loads(Koordinates)
            id=Koordinates['deviceID']
        time.sleep(60)

    