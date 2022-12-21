import logging
from concurrent import futures

from app.udaconnect import person_pb2
from app.udaconnect import person_pb2_grpc
from app.udaconnect.models import Person
from app.udaconnect.services import PersonService
import grpc
from typing import List

logger = logging.getLogger(__name__)

class PersonServicer(person_pb2_grpc.PersonService):
    def __init__(self, app):
        self.app = app

    def Get(self, request, context):
        persons = PersonService.retrieve_all_with_app(self.app)
        result = person_pb2.PersonMessageList()

        for person in persons: 
            grpc_person = person_pb2.PersonMessage(
                id = person.id,
                first_name = person.first_name,
                last_name = person.last_name,
                company_name = person.company_name
            )
            result.persons.extend([grpc_person])

        # FIXME: This must be mapped somehow!
        return result

class GrpcServer:
    def __init__(self, app): 
        self.app = app
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
        person_pb2_grpc.add_PersonServiceServicer_to_server(PersonServicer(self.app), self.server)

        self.server.add_insecure_port("[::]:5005")
        self.server.start()
