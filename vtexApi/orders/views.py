import logging
import json
import sys
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from utils import agenteKafka, agenteLogs

@api_view(['GET', 'POST'])
def obtenerPedidos(request):
    tema = settings.KAFKA_CONFIG['TOPIC']
    logs = agenteLogs.agenteLogs()
    kafka = agenteKafka.AgenteKafka()    
    try:
        if request.method == 'GET':
            logs.escribirLog('views: obtenerPedidos - HookVtex', 'Mensaje recibido desde el Hook, Mensaje: ' + str(request.method)+ ' - user: ' + str(request.user))
            data = {"data":"no avaliable"}
            return JsonResponse(data, safe=False)
        elif request.method == 'POST':
            logs.escribirLog('views: obtenerPedidos - HookVtex','Mensaje recibido desde el Hook, Mensaje: ' + str(request.data) + ' - user: ' + str(request.user))            
            data = request.data
            if not 'hookConfig' in data:
                kafkaRes= kafka.enviarMensajeKafka(tema,data)
                if(kafkaRes == False):
                    data ={"data":"Error al enviar Mensaje al Topic"}
                    logs.escribirLog(data, 'views: obtenerPedidos - kafka.sendMessageKafka')
                    return Response(data, status=status.HTTP_400_BAD_REQUEST)
                return Response(data, status=status.HTTP_201_CREATED)
            return Response(data, status=status.HTTP_201_CREATED)            
    except Exception as ex:
        logs.escribirLog("views: obtenerPedidos","Error al recibir o enviar el mensaje al agente kafka - error: " + str(ex))