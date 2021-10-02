from flask_app import app
from flask import render_template,redirect,request, session, flash
from flask_app.models.dojo import Dojos

@app.route("/")
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    return render_template('dojos.html', dojos=Dojos.get_all())

# Adding a new dojo to the list
@app.route('/create_dojo', methods=["POST"])
def create_dojo():
    data = {
        "dojo_name": request.form["dojo_name"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    Dojos.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/dojos')

@app.route('/dojos/show/<int:id>')
def show(id):
    data ={
        "id":id

    }
    return render_template("show_dojo.html", dojo=Dojos.get_one(data))
