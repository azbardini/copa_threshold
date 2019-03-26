# copa_threshold

O algoritmo faz uso da API do Copa para monitorar e realizar migração de containers de forma automatizada

# Como utilizar

Edite as seguintes primeiras linhas do treshold.py:

```
copaUrl = 'http://copaserver:8000/'
poolStart = 'Server2'
poolDestiny = 'Server1'
containerName = 'landoserver'
threshold = 10
```

**copaUrl**  é a URL do Copa Server.
**poolStart**  o nome do Copa Pool onde o container a ser migrado se encontra originalmente.
**poolDestiny** é o nome do Copa Pool para qual o container será migrado.
**containerName** é o nome do container a ser migrado na rede.
**treshold** é o limite em MB de throughput da rede em que, ao ser batido, inicia o processo de migração.
