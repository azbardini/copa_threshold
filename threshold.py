import requests
import json
import threading
import time 

#URL do Copa com a Porta para acesso RESTful
copaUrl = 'http://copaserver:8000/'

#Pool onde o server de video começa
poolStart = 'Server2'

#Pool para onde o server de video deve ser migrado
poolDestiny = 'Server1'

#Nome do container do server de video
containerName = 'landoserver'

#Treshold do throughput entre os Pools em MBPS
threshold = 10

def getThroughput():
    data = {}
    data['locus'] = poolStart
    data['last'] = '1'
    response = requests.get(copaUrl+'REST/network/kpilink', data)
    try: 
        throughput = response.json()['measurements'][0]['throughput']
    except:
        throughput = -1
    return throughput

def migrateContainer():
    print("Starting Migration")
    data = {
    "container_name": containerName,
    "container_pool": poolStart,
    "destination_pool": poolDestiny,
    "operation": "migrate"
    }
    result = requests.post(copaUrl+'REST/container', data).json()
    print(result) 

def checkMigration(throughput, treshold):
    shouldMigrate = "No"
    if throughput > threshold:
        shouldMigrate = "Yes"    
    return shouldMigrate

migratedYet = 'No'
while True:
    try:
        throughput = getThroughput()
    except:
        print("Error getting container info")
    shouldMigrate = checkMigration(throughput, threshold)
    print('Throughput: '+str(throughput)+ ' | Should migrate: '+ shouldMigrate+ ' | Migrated: '+migratedYet)
    if shouldMigrate == "Yes" and migratedYet == "No":
        migratedYet = "Yes"
        t = threading.Thread(target=migrateContainer)
        t.start()
    time.sleep(5)
