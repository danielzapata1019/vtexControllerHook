import logging
import json
from django.conf import settings
import time
import logging
import logging.handlers
from datetime import datetime

class agenteLogs():
    def __init__(self):
        dttime = datetime.now().strftime('%Y-%m-%d')
        log_file_name = settings.LOGS_FILENAME
        logs_Path = settings.LOGS_PATH
        logging_level = logging.DEBUG
        formatter = logging.Formatter('%(asctime)s - %(message)s')

        handler = logging.handlers.TimedRotatingFileHandler(logs_Path + log_file_name + '_' + dttime + '.log', when="d", interval=1, backupCount=10)
        handler.setFormatter(formatter)
        self.logger = logging.getLogger()
        self.logger.addHandler(handler)
        self.logger.setLevel(logging_level)

    def escribirLog(self,componente, mensaje):
        try:
            self.logger.info('componente: ' + componente + ' - Mensaje:  ' + mensaje)     
            return True
        except Exception as inst:
            self.logger.error(inst)
            return False
        finally:
            logging.shutdown()
