import os

from app import create_app
from app.udaconnect.kafka_consumer import MyKafkaConsumer

app = create_app(os.getenv("FLASK_ENV") or "test")
if __name__ == "__main__":
    kafka_consumer = MyKafkaConsumer(app)
    app.run(debug=False,host="0.0.0.0")
