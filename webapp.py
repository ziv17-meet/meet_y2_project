
from flask import Flask, render_template, request, redirect, url_for, session
from wtforms import *
from flask_wtf import Form
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import hashlib
import os


from database import *

current_directory = os.getcwd()
UPLOAD_FOLDER = os.path.join(current_directory, 'static/uploads')
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])




app = Flask(__name__)
engine = create_engine('sqlite:///crudlab.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'OASIUFHASIH087Y*&^(*&^OSIHUFD'

db = SQLAlchemy(app)

@app.route("/")
def show_homepage():
	



	return render_template('recipes.html')

@app.route("/about_us")
def about_us():
	return render_template("about_us.html")


@app.route("/main_dish", methods = ['GET', 'POST'])
def main_dish():
	main_dish_recipes = session.query(Recipes).filter_by(category="main_dish").all()
	return render_template("main_dish.html", main_dish_recipes=main_dish_recipes)



@app.route("/appetizers")
def appetizers():
	return render_template("appetizers.html")

@app.route("/specific/<int:id>/")
def specific(id):
	rec = session.query(Recipes).filter_by(id=id).all()
	return render_template("specific.html", rec=rec)



@app.route("/desserts", methods = ['GET', 'POST'])
def desserts():
	desserts_recipes = session.query(Recipes).filter_by(category="dessert").all()
	return render_template("desserts.html", desserts_recipes=desserts_recipes)

#@app.route("/desserts/<string:specialty>/")
#def desserts(specialty):
		#problem = session.query(Recipes).filter_by(special=specialty).all()
#	return render_template("desserts.html", problem=problem)

@app.route("/upload", methods = ['GET', 'POST']  )
def upload():

	if request.method == 'POST':
			category=request.form['category']
			ingredients=request.form['ingredients']
			#special=request.form['special']
			instructors=request.form['instructors']
			caption=request.form['caption']


			rec = Recipes(category=category, ingredients=ingredients, instructors=instructors, caption=caption)
			session.add(rec)
			session.commit()
			if category == 'dessert':
				return redirect("desserts")
			if category == 'main_dish':
				return redirect("main_dish")
			if category == 'appetizers':
				return redirect("appetizers")
			else:
				return render_template("upload.html")
	else:
		return render_template("upload.html")

@app.route("/pancake")
def pancake():
	return render_template("pancake_recepies.html")



if __name__ == '__main__':
	app.run(debug=True)
