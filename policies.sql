Terminal command:
$ sqlite3 dataFile/data.db
>>
CREATE TABLE policies (
    id INTEGER NOT NULL,
    policy_id INTEGER,
    date_of_purchase DATE,
    customer_id INTEGER,
    fuel VARCHAR,
    vehicle_segment VARCHAR,
    premium FLOAT,
    bodily_injury_liability INTEGER,
    personal_injury_protection INTEGER,
    property_damage_liability INTEGER,
    collision INTEGER,
    comprehensive INTEGER,
    customer_gender VARCHAR,
    customer_income_group VARCHAR,
    customer_region VARCHAR,
    customer_marital_status INTEGER,
    PRIMARY KEY (id)
);



# A generic, single database configuration.

[alembic]
# template used to generate migration files
# file_template = %%(rev)s_%%(slug)s

# set to 'true' to run the environment during
# the 'revision' command, regardless of autogenerate
# revision_environment = false


# Logging configuration
[loggers]
keys = root,sqlalchemy,alembic,flask_migrate

[handlers]
keys = console

[formatters]
keys = generic

[logger_root]
level = WARN
handlers = console
qualname =

[logger_sqlalchemy]
level = WARN
handlers =
qualname = sqlalchemy.engine

[logger_alembic]
level = INFO
handlers =
qualname = alembic

[logger_flask_migrate]
level = INFO
handlers =
qualname = flask_migrate

[handler_console]
class = StreamHandler
args = (sys.stderr,)
level = NOTSET
formatter = generic

[formatter_generic]
format = %(levelname)-5.5s [%(name)s] %(message)s
datefmt = %H:%M:%S

# The alembic section specifies configuration options for Alembic.

# The sqlalchemy.url setting specifies the database URL to use for migrations.
sqlalchemy.url = sqlite:///dataFile/data.db

# The target_metadata setting specifies the location of the models to use for migrations.
target_metadata = app.db.Model.metadata
