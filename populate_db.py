from app import app, db
from datetime import datetime
import json

# create the app context
app.app_context().push()

# open the JSON file
with open('dataFile/Insurance-Data.json', 'r') as f:
    data = json.load(f)

from dashboard.models import Policy
# iterate over the data and add each policy to the database
for policy_data in data:
    policy = Policy(**{
        "policy_id": policy_data["Policy_id"],
        "date_of_purchase": datetime.strptime(policy_data["Date of Purchase"], '%m/%d/%Y').date(),
        "customer_id": policy_data["Customer_id"],
        "fuel": policy_data["Fuel"],
        "vehicle_segment": policy_data["VEHICLE_SEGMENT"],
        "premium": policy_data["Premium"],
        "bodily_injury_liability": policy_data["bodily injury liability"],
        "personal_injury_protection": policy_data["personal injury protection"],
        "property_damage_liability": policy_data["property damage liability"],
        "collision": policy_data["collision"],
        "comprehensive": policy_data["comprehensive"],
        "customer_gender": policy_data["Customer_Gender"],
        "customer_income_group": policy_data["Customer_Income group"],
        "customer_region": policy_data["Customer_Region"],
        "customer_marital_status": policy_data["Customer_Marital_status"],
    })
    db.session.add(policy)

# commit the changes to the database
db.session.commit()
