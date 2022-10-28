import logging
from app.udaconnect.models import Person
from app.udaconnect.schemas import PersonSchema
from app.udaconnect.services import PersonService
from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import List

DATE_FORMAT = "%Y-%m-%d"

api = Namespace("UdaConnect Persons", description="PersonData.")  # noqa
logger = logging.getLogger(__name__)

@api.route("/persons")
class PersonsResource(Resource):
    @accepts("Person", schema=PersonSchema, api=api)
    @responds(schema=PersonSchema, api=api)
    def post(self) -> Person:
        new_person: Person = PersonService.create(api.payload)
        return new_person

    @responds(schema=PersonSchema, api=api, many=True)
    def get(self) -> List[Person]:
        persons: List[Person] = PersonService.retrieve_all()
        return persons


@api.route("/persons/<person_id>")
@api.param("person_id", "Unique ID for a given Person", _in="query")
class PersonResource(Resource):
    @responds(schema=PersonSchema, api=api)
    def get(self, person_id) -> Person:
        person: Person = PersonService.retrieve(person_id)
        return person
