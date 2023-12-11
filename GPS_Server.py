from socket import *
import json
import requests
serverport=12000
serversocket=socket(AF_INET,SOCK_DGRAM)
serversocket.bind(('',serverport))
baseurl="https://naturdanmark-api20231124193012.azurewebsites.net/Api/Coordinates"
print('Server Ready')



 
    
id=0
while True:
    Koordinates,clientAddress=serversocket.recvfrom(4048)
    print('message received')
    Koordinates=Koordinates.decode()
    Koordinates=json.loads(Koordinates)
    id=Koordinates['deviceID']
    if(Koordinates['deviceID']==0):
        id+=1
        response=requests.post(baseurl,json=Koordinates)
        serversocket.sendto(response.content,clientAddress)
    else:
        response=requests.put(baseurl +"/" + str(id),json=Koordinates)  
    print(Koordinates)
    print(response)  