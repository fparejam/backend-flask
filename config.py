import os

class Config:
    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:////home/fparejam/backend-flask/dataFile/data.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
