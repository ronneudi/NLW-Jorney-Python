from flask import jsonify, Blueprint

trips_bp = Blueprint("trips_routes", __name__)


@trips_bp.route("/trips", methods=["POST"])
def create_trips():
    return jsonify({"status": "OK"})
