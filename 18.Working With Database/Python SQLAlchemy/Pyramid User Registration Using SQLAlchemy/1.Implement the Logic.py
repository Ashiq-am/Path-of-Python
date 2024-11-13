from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.renderers import render_to_response
from pyramid.view import view_config
from pyramid.session import SignedCookieSessionFactory

import sqlalchemy as db
from sqlalchemy.dialects.sqlite import *
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

import os
import re


# Database Engine
engine = db.create_engine("sqlite:///users.db", echo=True)
Base = declarative_base()

# Model Class
class Applicants(Base):
	__tablename__ = "applicant"
	id = db.Column(db.Integer, primary_key=True, nullable=False)
	name = db.Column(db.String(63), unique=False)
	email = db.Column(db.String(63), unique=True)
	mobile = db.Column(db.String(10), unique=True)

	# For Formatting the Output in JSON Format
	def to_dict(self):
		return {
			"id": self.id,
			"name": self.name,
			"email": self.email,
			"mobile": self.mobile,
		}


# Check if database exists
if os.path.exists("users.db"):
	print("Database already exists!")
else:
	# Create database
	Base.metadata.create_all(engine)


@view_config(route_name="register", renderer="index.html")
def registration(request):
	if request.method == "POST":
		name = request.POST["name"]
		email = request.POST["email"]
		mobile = request.POST["mobile"]

		# For Pattern Matching, Input Validation
		emailPattern = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
		mobilePattern = re.compile(r"^[0-9]{10}$")

		if name != "" and emailPattern.match(email) and mobilePattern.match(mobile):
			request.session["name"] = request.POST["name"]
			request.session["email"] = request.POST["email"]

			# Insert into database
			session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
			s = session()

			commonEmail = s.query(Applicants).filter_by(email=email).first()
			commonMobile = s.query(Applicants).filter_by(mobile=mobile).first()

			if commonEmail is not None or commonMobile is not None:
				request.session.flash("User is already registered!")

				return render_to_response(
					"index.html",
					{"error": "User is already registered!"},
					request=request,
				)

			# Insert into database
			applicant = Applicants(name=name, email=email, mobile=mobile)
			s.add(applicant)
			s.commit()
			s.close()

			request.session.flash("Success!")
			return render_to_response(
				"proceed.html", {"error": "Success!"}, request=request
			)
		else:
			request.session.flash("Please fill in all fields properly!")
			return render_to_response(
				"index.html",
				{"error": "Please fill in all fields properly!"},
				request=request,
			)
	else:
		return render_to_response("index.html", {}, request=request)


@view_config(route_name="proceed", renderer="proceed.html")
def proceed(request):
	return render_to_response("proceed.html", {}, request=request)


@view_config(route_name="dashboard", renderer="dashboard.html")
def dashboard(request):
	if request.method == "POST":
		session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
		s = session()

		# Delete in database
		if request.POST["button"] == "delete" and request.POST["emailForDelete"]:
			emailForDelete = request.POST["emailForDelete"]

			applicant = s.query(Applicants).filter_by(email=emailForDelete).first()
			s.delete(applicant)

			request.session.flash("Deleted!")

		# Update in database
		elif request.POST["button"] == "update" and request.POST["emailForUpdate"]:
			emailForUpdate = request.POST["emailForUpdate"]

			applicant = s.query(Applicants).filter_by(email=emailForUpdate).first()
			applicant.name = request.POST["name"]
			applicant.email = request.POST["email"]
			applicant.mobile = request.POST["mobile"]

			request.session.flash("Updated!")

		s.commit()
		s.close()

	# Fetch from database
	Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
	s = Session()

	applicants = s.query(Applicants).all()
	applicants_data = [applicant.to_dict() for applicant in applicants]
	s.close()

	request.session["data"] = applicants_data

	return render_to_response("dashboard.html", {}, request=request)


my_session = SignedCookieSessionFactory("mySession")

if __name__ == "__main__":
	with Configurator() as config:
		# Initialize Session Factory
		config.set_session_factory(my_session)

		# Add Jinja2 Template Renderer
		config.include("pyramid_jinja2")
		config.add_jinja2_renderer(".html")

		# Add Routes and Views
		config.add_route("register", "/")
		config.add_view(registration, route_name="register")

		config.add_route("proceed", "/proceed.html")
		config.add_view(proceed, route_name="proceed")

		config.add_route("dashboard", "/dashboard.html")
		config.add_view(dashboard, route_name="dashboard")

		config.scan("flash")

		app = config.make_wsgi_app()

	server = make_server("0.0.0.0", 6543, app)
	server.serve_forever()
