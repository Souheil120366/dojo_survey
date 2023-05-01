from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo import Dojo


@app.route("/")
def index():
    return redirect('/dojos/new')



@app.route("/result")
def dojo_show():
    dojo_to_show = Dojo.get_one()
    return render_template("dojo_show.html",dojo=dojo_to_show)


@app.route('/dojos/new')
def create_dojo():
    return render_template("dojos.html")

@app.route("/dojos/create",methods=['POST'])
def new_dojo():
    print(request.form)
    if not Dojo.validate_dojo(request.form):
        # redirect to the route where the dojo form is rendered.
        return redirect('/')
    Dojo.save(request.form)
    return redirect('/result')
