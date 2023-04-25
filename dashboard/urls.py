from dashboard.service import get_all_policies
from flask import jsonify
from flask import request

def initialize_routes(app):
    @app.route('/api/policies')
    def get_policies():
        policies = get_all_policies()
        return jsonify(policies)
    
    possible_groups= ["0- $25K","$25-$70K",">$70K"]    
    @app.route('/api/income')
    def get_filtered_policies():
        #Get income and what group the policies that we are interested in are.
        income = int(request.args.get('income'))
        print(income)
        if income < 25:
            group = possible_groups[0]
        elif income > 25 and income < 70:
            group = possible_groups[1]
        else:
            group = possible_groups[2]

        policies = get_all_policies()
        filtered_policies_by_income = []
        for policy in policies:
            if policy.customer_income_group == group:
                filtered_policies_by_income.append(policy)

        return jsonify(filtered_policies_by_income)
