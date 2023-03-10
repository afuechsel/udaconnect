import logging
from typing import Dict, List

from app import db
from app.udaconnect.models import Person

logger = logging.getLogger(__name__)

class PersonService:
    @staticmethod
    def create(person: Dict) -> Person:
        new_person = Person()
        new_person.first_name = person["first_name"]
        new_person.last_name = person["last_name"]
        new_person.company_name = person["company_name"]

        db.session.add(new_person)
        db.session.commit()

        return new_person

    @staticmethod
    def retrieve(person_id: int) -> Person:
        person = db.session.query(Person).get(person_id)
        return person

    @staticmethod
    def retrieve_all() -> List[Person]:
        return db.session.query(Person).all()

    @staticmethod
    def retrieve_all_with_app(app) -> List[Person]:
        with app.app_context():
            return db.session.query(Person).all()
