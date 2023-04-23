from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config
from dashboard.urls import initialize_routes
from database import db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

# enable CORS
CORS(app)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

# initialize routes
initialize_routes(app)

if __name__ == '__main__':
    app.run()
