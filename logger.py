import os
from time import sleep, strftime
import requests
import xml.etree.ElementTree as xml
import sqlalchemy as db
from sqlalchemy import *

if not os.getenv("API_ENDPOINT"):
    from dotenv import load_dotenv
    load_dotenv()

# Define a means to get the required data
url = os.getenv("API_ENDPOINT")


# Function that returns new data from the endpoint
def getData():
    try:
        return requests.get(url).content
    except Exception as e:
        print("API Fetch Error", e)
        pass


# Create the DB engine and connect to the DB
engine = db.create_engine('{}://{}:{}@{}:{}/{}'.format(
                          *map(os.getenv, ["DB_ENGINE", "DB_USERNAME",
                                           "DB_PASSWORD", "DB_HOST",
                                           "DB_PORT", "DB_NAME"])))
connection = engine.connect()

# Create the table if it doesn't already exist
# datapoints = ['LoggedAt', 'TrainStatus', 'TrainLatitude', 'TrainLongitude',
#               'TrainCode', 'TrainDate', 'PublicMessage', 'Direction']
db_metadata = MetaData()
datapoints = Table('datapoints', db_metadata,
                   Column('id', Integer, primary_key=True),
                   Column('LoggedAt', DateTime),
                   Column('TrainStatus', String(1)),
                   Column('TrainLatitude', Float),
                   Column('TrainLongitude', Float),
                   Column('TrainCode', String(255)),
                   Column('TrainDate', String(11)),
                   Column('PublicMessage', Text),
                   Column('Direction', String(255))
                   )
db_metadata.create_all(engine)

previous_data = []
changeset = []
while 1:
    # Fetch the data
    raw_data = getData()

    # Parse the XML into a dict
    try:
        trains = list(map(lambda train: dict(map(lambda datapoint: (
            datapoint.tag.split('}')[-1], datapoint.text.replace("\\n", "\n")),
            train)),
            xml.fromstring(raw_data)))
    except Exception as e:
        print("XML Parse Error", e)
        sleep(5)
        continue
    new_data = trains

    # The changeset contains all data not in the previous dataframe
    changeset += [dict(train, LoggedAt=strftime("%Y-%m-%d %H:%M:%S"))
                  for train in filter(
        (lambda x: x not in previous_data), new_data)]

    # Store all this data in the DB
    if changeset:
        try:
            connection.execute(
                datapoints.insert(changeset))
            changeset = []
        except Exception as e:
            print("DB Insert Failure", e)
            pass

    # Store the new dataframe to compare the nexy one
    previous_data = trains

    # Wait a few seconds until we check if anything has changed
    sleep(5)
