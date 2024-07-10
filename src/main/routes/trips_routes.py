from flask import jsonify, Blueprint, request
from src.controllers.trip_creator import TripCreator
from src.controllers.trip_finder import TripFinder
from src.controllers.trip_confirmer import TripConfirmer
from src.controllers.link_creator import LinkCreator
from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.email_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.links_repository import LinksRepository
from src.models.settings.db_connection_handler import db_connection_handler

trips_bp = Blueprint("trips_routes", __name__)


@trips_bp.route("/trips", methods=["POST"])
def create_trips():
    conn = db_connection_handler.get_connection()
    trips_repo = TripsRepository(conn)
    emails_repo = EmailsToInviteRepository(conn)
    controller = TripCreator(trips_repo, emails_repo)
    response = controller.create(request.json)
    return jsonify(response["body"]), response["status_code"]


@trips_bp.route("/trips/<trip_id>", methods=["GET"])
def finder_trips(trip_id):
    conn = db_connection_handler.get_connection()
    trips_repo = TripsRepository(conn)
    controller = TripFinder(trips_repo)
    response = controller.find_trip_details(trip_id)
    return jsonify(response["body"]), response["status_code"]


@trips_bp.route("/trips/<trip_id>/link", methods=["POST"])
def create_trip_link(trip_id):
    conn = db_connection_handler.get_connection()
    links_repo = LinksRepository(conn)
    controller = LinkCreator(links_repo)
    response = controller.creator(request.json, trip_id)
    return jsonify(response["body"]), response["status_code"]


@trips_bp.route("/trips/<trip_id>/confirm", methods=["GET"])
def confirm_trip(trip_id):
    conn = db_connection_handler.get_connection()
    trips_repo = TripsRepository(conn)
    controller = TripConfirmer(trips_repo)
    response = controller.confirm(trip_id)
    return jsonify(response["body"]), response["status_code"]
