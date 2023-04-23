from dashboard.service import get_all_policies
from flask import jsonify

def initialize_routes(app):
    @app.route('/api/policies')
    def get_policies():
        policies = get_all_policies()
        return jsonify(policies)
