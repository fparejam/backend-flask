from sqlalchemy import Column, Integer, String, Date, Float
from database import db

class Policy(db.Model):
    __tablename__ = 'policies'

    id = Column(Integer, primary_key=True)
    policy_id = Column(Integer)
    date_of_purchase = Column(Date)
    customer_id = Column(Integer)
    fuel = Column(String)
    vehicle_segment = Column(String)
    premium = Column(Float)
    bodily_injury_liability = Column(Integer)
    personal_injury_protection = Column(Integer)
    property_damage_liability = Column(Integer)
    collision = Column(Integer)
    comprehensive = Column(Integer)
    customer_gender = Column(String)
    customer_income_group = Column(String)
    customer_region = Column(String)
    customer_marital_status = Column(Integer)
