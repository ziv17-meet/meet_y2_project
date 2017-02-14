
from flask import Flask, render_template, request, redirect, url_for, session
#from wtforms import *
#from flask_wtf import Form
#from flask_sqlalchemy import SQLAlchemy
#from werkzeug.utils import secure_filename
#import hashlib
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

#db = SQLAlchemy(app)

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

	if request.method == 'POST':

		special=request.form['special']

		if special == 'suggar_free':
			filter_suggar = session.query(Recipes).filter_by(special="suggar_free").all()
			return render_template("main_dish.html", filter_suggar=filter_suggar)
		if special == 'glutten_free':
			filter_glutten = session.query(Recipes).filter_by(special="glutten_free").all()
			return render_template("main_dish.html", filter_glutten=filter_glutten)
		if special == 'viggen':
			filter_viggen = session.query(Recipes).filter_by(special="viggen").all()
			return render_template("main_dish.html", filter_viggen=filter_viggen)
		else:
			return render_template("main_dish.html")
	else:
		return render_template("main_dish.html")


@app.route("/appetizers")
def appetizers():
	appetizers_recipes = session.query(Recipes).filter_by(category="appetizers").all()
	return render_template("appetizers.html", appetizers_recipes=appetizers_recipes)
	if request.method == 'POST':
		special=request.form['special']
		rec = Recipes(special=special)
		session.add(rec)
		session.commit()
		if special == 'suggar_free':
			filter_suggar = session.query(Recipes).filter_by(special="suggar_free").all()
			return render_template("appetizers.html", filter_suggar=filter_suggar)
		if special == 'glutten_free':
			filter_glutten = session.query(Recipes).filter_by(special="glutten_free").all()
			return render_template("appetizers.html", filter_glutten=filter_glutten)
		if special == 'viggen':
			filter_viggen = session.query(Recipes).filter_by(special="viggen").all()
			return render_template("appetizers.html", filter_viggen=filter_viggen)
		else:
			return render_template("appetizers.html")
	else:
		return render_template("appetizers.html")



@app.route("/specific/<int:id>/")
def specific(id):
	rec = session.query(Recipes).filter_by(id=id).all()
	return render_template("specific.html", rec=rec)
	if request.method == 'POST':
			comments=request.form['comments']
			rec = Recipes(comments=comments)
			session.add(rec)
			session.commit()
			return redirect("specific", rec=rec)

	else:
		return render_template("upload.html")

@app.route("/upload", methods = ['GET', 'POST']  )
def upload():

	if request.method == 'POST':
			category=request.form['category']
			ingredients=request.form['ingredients']
			special=request.form['special']
			instructors=request.form['instructors']
			caption=request.form['caption']


			rec = Recipes(category=category, ingredients=ingredients, instructors=instructors, caption=caption, special=special)
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
@app.route("/desserts", methods = ['GET', 'POST'])
def desserts():
	desserts_recipes = session.query(Recipes).filter_by(category="dessert").all()
	return render_template("desserts.html", desserts_recipes=desserts_recipes)
	if request.method == 'POST':
		special=request.form['special']
		rec = Recipes(special=special)
		session.add(rec)
		session.commit()
		if special == 'suggar_free':
			filter_suggar = session.query(Recipes).filter_by(special="suggar_free").all()
			return redirect("desserts.html", filter_suggar=filter)
		if special == 'glutten_free':
			filter_glutten = session.query(Recipes).filter_by(special="glutten_free").all()
			return redirect("desserts.html", filter_glutten=filter)
		if special == 'viggen':
			filter_viggen = session.query(Recipes).filter_by(special="viggen").all()
			return redirect("desserts.html", filter_viggen=filter)
		if special == 'suggar_free' and 'glutten_free':
			filter_suggar_free_glutten_free = session.query(Recipes).filter_by(special="suggar_free glutten_free").all()
			return redirect("desserts.html", filter_suggar_free_glutten_free=filter)
		if special == 'viggen' and 'glutten_free':
			filter_viggen_glutten_free = session.query(Recipes).filter_by(special="viggen glutten_free").all()
			return redirect("desserts.html", filter_viggen_glutten_free=filter_viggen_glutten_free)
		if special == 'viggen'and 'suggar_free':
			filter_viggen_suggar_free = session.query(Recipes).filter_by(special="viggen suggar_free").all()
			return redirect("desserts.html", filter_viggen_suggar_free=filter)
		if special == 'viggen'and 'suggar_free' and 'glutten_free':
			filter_viggen_suggar_free_glutten_free = session.query(Recipes).filter_by(special="viggen suggar_free glutten_free").all()
			return redirect("desserts.html", filter_viggen_suggar_free_glutten_free=filter)
		else:
			return render_template("desserts.html")
	else:
		return render_template("desserts.html")


#@app.route("/desserts/<string:specialty>/")
#def desserts(specialty):
		#problem = session.query(Recipes).filter_by(special=specialty).all()
#	return render_template("desserts.html", problem=problem)



@app.route("/pancake")
def pancake():
	return render_template("pancake_recepies.html")



if __name__ == '__main__':
	app.run(debug=True)
