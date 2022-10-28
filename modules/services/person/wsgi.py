import os

from app import create_app
from app.udaconnect.grpc import GrpcServer

app = create_app(os.getenv("FLASK_ENV") or "test")
if __name__ == "__main__":
    grpc_server = GrpcServer(app)
    app.run(debug=True,host="0.0.0.0")
