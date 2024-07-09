from flask import Flask
from ..routes.trips_routes import trips_bp

app = Flask(__name__)
app.register_blueprint(trips_bp)
