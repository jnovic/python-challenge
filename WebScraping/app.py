#import dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars 

#setup Flask and mongodb connection
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/db"
mongo = PyMongo(app)

@app.route("/")
def index():
    facts = mongo.db.factoids.find_one()
    return render_template("index.html", facts=facts)


@app.route("/scrape")
def scrape():
    mars = mongo.db.factoids
    facts_data = scrape_mars.scrape()
    mars.update({}, facts_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)




