# service.py
from dashboard.models import Policy
from database import db

def get_all_policies():
    print('Request received')
    policies = Policy.query.all()
    policy_list = []
    for policy in policies:
        policy_dict = {
            'Policy_id': policy.policy_id,
            'Date of Purchase': str(policy.date_of_purchase),
            'Customer_id': policy.customer_id,
            'Fuel': policy.fuel,
            'VEHICLE_SEGMENT': policy.vehicle_segment,
            'Premium': policy.premium,
            'bodily injury liability': policy.bodily_injury_liability,
            'personal injury protection': policy.personal_injury_protection,
            'property damage liability': policy.property_damage_liability,
            'collision': policy.collision,
            'comprehensive': policy.comprehensive,
            'Customer_Gender': policy.customer_gender,
            'Customer_Income group': policy.customer_income_group,
            'Customer_Region': policy.customer_region,
            'Customer_Marital_status': policy.customer_marital_status
        }
        policy_list.append(policy_dict)
    return policy_list
