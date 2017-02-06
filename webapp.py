
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

@app.route("/main_dish")
def main_dish():
	return render_template("main_dish.html")

@app.route("/appetizers")
def appetizers():
	return render_template("appetizers.html")

@app.route("/specific/<int:id>/")
def specific(id):
	spec = session.query(Recipes).filter_by(id=id).first()
	return render_template("specific.html", spec=spec)



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
			category=request.form['catagory']
			ingredients_list=[request.form['ingredient1'], request.form['ingredient2'], request.form['ingredient3']]
			ingredients='<delim>'.join(ingredients_list)
			images=request.form['images']
			special=request.form['special']
			instructors_list=[request.form['instructor1'], request.form['instructor2'], request.form['instructor3']]
			instuctors='<delim>'.join(instructor_list)
			caption=request.form['caption']


			rec = Recipes(category=category, ingredient1=ingredient1, ingredient2=ingredient2, ingredient3=ingredient3, images=images, special=specia, instuctor1=instuctor1, instructor2=instructor2, instructor3=instructor3, caption=caption)
			session.add(rec)
			session.commit()
			if category == 'dessert':
				return render_template("dessert.html", rec=rec)
			if category == 'main_dish':
				return render_template("main_dish.html", rec=rec)
			if category == 'appetizers':
				return render_template("appetizers.html", rec=rec)
			else:
				return render_template("upload.html")
	else:
		return render_template("upload.html")

@app.route("/pancake")
def pancake():
	return render_template("pancake_recepies.html")



if __name__ == '__main__':
	app.run(debug=True)
