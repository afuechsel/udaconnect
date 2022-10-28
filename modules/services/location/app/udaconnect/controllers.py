from app.udaconnect.models import Location
from app.udaconnect.schemas import LocationSchema
from app.udaconnect.services import LocationService
from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource

api = Namespace("UdaConnect Locations", description="Geolocations")  # noqa

@api.route("/locations")
class LocationsResource(Resource):
    @accepts("Location", schema=LocationSchema, api=api)
    @responds(schema=LocationSchema, api=api)
    def post(self) -> Location:
        location: Location = LocationService.create(api.payload)
        return location

@api.route("/locations/<location_id>")
@api.param("location_id", "Unique ID for a given Location", _in="query")
class LocationResource(Resource):
    @responds(schema=LocationSchema, api=api)
    def get(self, location_id) -> Location:
        location: Location = LocationService.retrieve(location_id)
        return location