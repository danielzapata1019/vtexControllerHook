from kafka import KafkaProducer
from django.conf import settings
from utils import agenteLogs
import json


class AgenteKafka:
    def __init__(self):
         self.kafkaBroker = settings.KAFKA_CONFIG['BOOOTSTRAP_SERVERS_KAFKA']
         self.logs = agenteLogs.agenteLogs()
         self.productor = self.conectar_productor_kafka()
         
    
    def conectar_productor_kafka(self):
        productor = None        
        try:
            productor = KafkaProducer(bootstrap_servers=self.kafkaBroker)
        except Exception as ex:
            self.logs.escribirLog('AgenteKafka:conectar_productor_kafka',"Error durante conexion con kafka- error: " + str(ex))
        finally:
            return productor

    def enviarMensajeKafka(self, topic, data):
        try:
            print(str(data))   
            response= True          
            """response = self.productor.send(topic, json.dumps(data)).add_callback(
                self.on_success).add_errback(self.on_error)"""
            self.productor.flush()
            if self.productor is not None:
                self.productor.close()        
            return response
        except Exception as ex:
            self.logs.escribirLog('AgenteKafka: enviarMensajeKafka',"Error al enviar mensaje al topic - error: " + str(ex))
            return True

    def on_success(self,record_metadata):
        self.logs.escribirLog('AgenteKafka: on_success','Mensaje Enviado al Topic')
        return True

    def on_error(self,excp):
        self.logs.escribirLog("AgenteKafka: on_error", "Ocurrio un error al enviar mensaje al Topic"+ str(excp))
        return False