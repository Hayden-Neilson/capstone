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

ENV = 'dev'
if ENV =='dev':
  app.debug = True
  app.config["SQLALCHEMY_DATABASE_URI"] = "http://127.0.0.1:5000/postgresql:/postgres:Hneilson1@localhost/Capstone"
else:
  app.debug = False
  app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Job(db.Model):
  __tablename__ = "scraped_info"
  id = db.Column(db.Integer, primary_key=True)
  job = db.Column(db.String(100), nullable=False)
  salary = db.Column(db.String(500))
  company = db.Column(db.String(130))



#   def __init__(self, , salary, company ):  
#     self.salary = salary
#     self.company = company


# class Schema(ma.Schema):
#   class Meta:
#     fields = ("id",  "salary" "Company",)

# job_schema = JobSchema()
# jobs_schema = Schema(many=True)

# @app.route("/", methods=["GET"])
# def home():
#   return "<h1>Capstone API</h1>"

# # GET
# @app.route("/", methods=["GET"])
# def get_():
#   all_jobs = jobs.query.all()
#   result = _schema.dump(all_)
#   return jsonify(result)

#   # Get one by the id

# @app.route("//<id>", methods=["GET"])
# def get_job(id):
#    get_job = job.query.get(id)

#   result = job_schema.dump()
#   return jsonify(result)


# # POST
# @app.route("/add-job", methods=["POST"])
# def add_job():

#   salary = request.json["salary"]
#   company = request.json["company"]



#   new_job = (title, salary, company, Location )

#   db.session.add(new_job)
#   db.session.commit()

#    = .query.get(new_.id)
#   return _schema.jsonify()



# # PUT / PATCH

# @app.route("//<id>", methods=["PATCH"])
# def update_job(id):
#    update_job= job.query.get(id)

#   modified_job = request.json["updated job"]

#   . = modified_job

#   db.session.commit()

#   return _schema.jsonify()


# # DELETE

# @app.route("/delete/<id>", methods=["DELETE"])
# def remove_job(id):
#   record = .query.get(id)
#   db.session.delete(record)
#   db.session.commit()

#   return jsonify("delete that ish")

if __name__ == "__main__":
  app.run()