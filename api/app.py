from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_heroku import Heroku
from environs import Env
import os

app = Flask(__name__)
CORS(app)
heroku = Heroku(app)

env = Env()
env.read_env()
DATABASE_URL = env("DATABASE_URL")



basedir = os.path.abspath(os.path.dirname(__file__))
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "app.sqlite")
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Job(db.Model):
  __tablename__ = "jobs"
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  job_description = db.Column(db.String(500))
  company_name = db.Column(db.String(130))
  location = db.Column(db.String(50)


  def __init__(self, title, job_description, Company, Location):
    self.title = title
    self.job_description = job_description
    self.Company_name = company_name
    self.Location = location

class Schema(ma.Schema):
  class Meta:
    fields = ("id", "title", "salary" "Company", "Location")

job_schema = JobSchema()
jobs_schema = Schema(many=True)

@app.route("/", methods=["GET"])
def home():
  return "<h1>Capstone API</h1>"

# GET
@app.route("/", methods=["GET"])
def get_():
  all_jobs = jobs.query.all()
  result = _schema.dump(all_)
  return jsonify(result)

  # Get one by the id

@app.route("//<id>", methods=["GET"])
def get_job(id):
   get_job = job.query.get(id)

  result = job_schema.dump()
  return jsonify(result)


# POST
@app.route("/add-job", methods=["POST"])
def add_job():
  title = request.json["title"]
  job_description = request.json["job_description"]
  company = request.json["company"]
  location = request.json["location"]


  new_job = (title, job_description, Company, Location )

  db.session.add(new_job)
  db.session.commit()

   = .query.get(new_.id)
  return _schema.jsonify()



# PUT / PATCH

@app.route("//<id>", methods=["PATCH"])
def update_job(id):
   update_job= job.query.get(id)

  modified_job = request.json["updated job"]

  . = modified_job

  db.session.commit()

  return _schema.jsonify()


# DELETE

@app.route("/delete/<id>", methods=["DELETE"])
def remove_job(id):
  record = .query.get(id)
  db.session.delete(record)
  db.session.commit()

  return jsonify("delete that ish")

if __name__ == "__main__":
  app.debug = True
  app.run()