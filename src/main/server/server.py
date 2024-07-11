from flask import Flask
from ..routes.trips_routes import trips

app = Flask(__name__)
app.register_blueprint(trips)
