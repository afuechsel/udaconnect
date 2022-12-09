import json
import threading
import logging
from kafka import KafkaConsumer

from app.udaconnect.services import LocationService

TOPIC_NAME = 'locations'
KAFKA_SERVER = 'kafka:9093'

logger = logging.getLogger(__name__)

# reduce the log level for kafka
kafka_logger = logging.getLogger('kafka')
kafka_logger.setLevel(logging.WARN)

class MyKafkaConsumer: 
    def __init__(self, app):
        self.app = app
        logger.info("Creating kafka consumer for topic " + TOPIC_NAME)
        self.consumer = KafkaConsumer(TOPIC_NAME, 
            bootstrap_servers=KAFKA_SERVER, 
            client_id="udaconnect",
            fetch_max_wait_ms=30000,
            enable_auto_commit=True,
            auto_commit_interval_ms=500,
            auto_offset_reset="latest",
            value_deserializer=lambda m: json.loads(m.decode('utf-8')))

        # start consumer thread
        t = threading.Thread(target=self.consume)
        t.start()

    def consume(self): 
        while True:
            try: 
                for message in self.consumer:
                    logger.info(message.value)
                    with self.app.app_context(): 
                        LocationService.create(message.value)
            except Exception as error: 
                logger.error(error)
    