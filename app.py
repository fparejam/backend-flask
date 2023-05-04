from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config
from dashboard.urls import initialize_routes
from dashboard.bigram_service import load_bigram_model, generate_text
from database import db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

# enable CORS
CORS(app)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

# load the bigram model
bigram_model = load_bigram_model('bigram_model1.pth')

# initialize routes
initialize_routes(app)

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.get_json()
    context = data.get('context', '')
    generated_text = generate_text(bigram_model, context)
    return jsonify({'generated_text': generated_text})

if __name__ == '__main__':
    app.run()
