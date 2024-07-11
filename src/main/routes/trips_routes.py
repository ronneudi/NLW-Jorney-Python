from flask import jsonify, Blueprint, request
from src.controllers.activity_creator import ActivityCreator
from src.controllers.activiy_finder import ActivityFinder
from src.controllers.link_creator import LinkCreator
from src.controllers.link_finder import LinkFinder
from src.controllers.participant_creator import ParticipantCreator
from src.controllers.participant_finder import ParticipantFinder
from src.controllers.trip_creator import TripCreator
from src.controllers.trip_finder import TripFinder
from src.controllers.trip_confirmer import TripConfirmer
from src.controllers.participant_confirmer import ParticipantConfirmer
from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.email_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.participants_repository import ParticipantsRepository
from src.models.repositories.links_repository import LinksRepository
from src.models.repositories.activities_repository import ActivitiesRepository
from src.models.settings.db_connection_handler import db_connection_handler

trips = Blueprint(name="trips_routes", import_name=__name__, url_prefix='/trips')


@trips.route("/", methods=["POST"])
def create_trips():
    conn = db_connection_handler.get_connection()
    trips_repo = TripsRepository(conn)
    emails_repo = EmailsToInviteRepository(conn)
    controller = TripCreator(trips_repo, emails_repo)
    response = controller.create(request.json)
    return jsonify(response["body"]), response["status_code"]


@trips.route("/", methods=["GET"])
def list_trips():
    conn = db_connection_handler.get_connection()
    trips_repo = TripsRepository(conn)
    controller = TripFinder(trips_repo)
    response = controller.find_all_trips_detail()
    return jsonify(response["body"]), response["status_code"]


@trips.route("/<trip_id>", methods=["GET"])
def finder_trips(trip_id):
    conn = db_connection_handler.get_connection()
    trips_repo = TripsRepository(conn)
    controller = TripFinder(trips_repo)
    response = controller.find_trip_details(trip_id)
    return jsonify(response["body"]), response["status_code"]


@trips.route("/<trip_id>/confirm", methods=["GET"])
def confirm_trip(trip_id):
    conn = db_connection_handler.get_connection()
    trips_repo = TripsRepository(conn)
    controller = TripConfirmer(trips_repo)
    response = controller.confirm(trip_id)
    return jsonify(response["body"]), response["status_code"]


@trips.route("/<trip_id>/links", methods=["GET"])
def find_trip_link(trip_id):
    conn = db_connection_handler.get_connection()
    links_repo = LinksRepository(conn)
    controller = LinkFinder(links_repo)
    response = controller.find(trip_id)
    return jsonify(response["body"]), response["status_code"]


@trips.route("/<trip_id>/links", methods=["POST"])
def create_trip_link(trip_id):
    conn = db_connection_handler.get_connection()
    links_repo = LinksRepository(conn)
    controller = LinkCreator(links_repo)
    response = controller.creator(request.json, trip_id)
    return jsonify(response["body"]), response["status_code"]


@trips.route("/<trip_id>/invites", methods=["POST"])
def invite_to_trip(trip_id):
    conn = db_connection_handler.get_connection()
    participants_repo = ParticipantsRepository(conn)
    emails_repo = EmailsToInviteRepository(conn)
    controller = ParticipantCreator(participants_repo, emails_repo)
    response = controller.create(request.json, trip_id)
    return jsonify(response["body"]), response["status_code"]


@trips.route("/<trip_id>/activities", methods=["POST"])
def create_activity(trip_id):
    conn = db_connection_handler.get_connection()
    act_repo = ActivitiesRepository(conn)
    controller = ActivityCreator(act_repo)
    response = controller.create(request.json, trip_id)
    return jsonify(response["body"]), response["status_code"]


@trips.route("/<trip_id>/activities", methods=["GET"])
def get_trip_activities(trip_id):
    conn = db_connection_handler.get_connection()
    act_repo = ActivitiesRepository(conn)
    controller = ActivityFinder(act_repo)
    response = controller.find_activities_from_trip(trip_id)
    return jsonify(response["body"]), response["status_code"]


@trips.route("/<trip_id>/participanties", methods=["GET"])
def get_participanties(trip_id):
    conn = db_connection_handler.get_connection()
    part_repo = ParticipantsRepository(conn)
    controller = ParticipantFinder(part_repo)
    response = controller.find_participants_from_trip(trip_id)
    return jsonify(response["body"]), response["status_code"]


@trips.route("/<trip_id>/participanties/<participant_id>/confirm", methods=["PATCH"])
def confirm_participant(trip_id, participant_id):
    conn = db_connection_handler.get_connection()
    part_repo = ParticipantsRepository(conn)
    controller = ParticipantConfirmer(part_repo)
    response = controller.confirm(participant_id, trip_id)
    return jsonify(response['body']), response['status_code']
