import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

from flask import Flask, jsonify

#get my session up and running
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create our session (link) from Python to the DB
session = Session(engine)
fecha = dt.date(2017, 8, 23) - dt.timedelta(days=365)

app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start> %Y-%m-%d<br/>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    sel = [Measurement.date, Measurement.prcp]
    aug_23_2017 = session.query(*sel).filter(Measurement.date >= fecha).all()
    prcpflask = []
    for d in aug_23_2017:
        prcpflask.append({"date": d[0], "prcp":d[1]})
    return jsonify(prcpflask)

@app.route("/api/v1.0/stations")
def stations():
    station_data = session.query(Station.station, Station.name).all()
    station_list =[]
    for s in station_data:
        station_list.append({"Station_ID":s[0], "Station_Name":s[1]})
    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def tobs():
    monthtemp = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= fecha).all()
    temp_list = []
    for t in monthtemp:
        temp_list.append({"date":[0], "temp":[1]})
    return jsonify(temp_list)

@app.route("/api/v1.0/<start>")
def start(start):
    maxminavg = session.query(func.max(Measurement.tobs),func.min(Measurement.tobs),\
    func.avg(Measurement.tobs)).filter(Measurement.date >= start).all()
    summarytemp1 = []
    for i in maxminavg:
        summarytemp1.append({"tmax":i[0], "tmin":i[1], "tavg":i[2]})
    return jsonify(summarytemp1)

@app.route("/api/v1.0/<start>/<end>")
def end(start, end):
    maxminavg2 = session.query(func.max(Measurement.tobs),func.min(Measurement.tobs),\
    func.avg(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    summarytemp2 = []
    for j in maxminavg2:
        summarytemp2.append({"tmax":j[0], "tmin":j[1], "tavg":j[2]})
    return jsonify(summarytemp2)


if __name__ == '__main__':
    app.run(debug=True)
