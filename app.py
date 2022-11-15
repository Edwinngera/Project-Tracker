from flask import Flask,render_template
from forms import ConfirmationForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config




app=Flask(__name__)
app.config.from_object(Config)
from models import db,Projects
db.init_app(app) #Add this line Before migrate line
migrate = Migrate(app, db)



@app.route("/")
def home():
    
    return render_template('home.html',title="Dashboard")

@app.route("/charts")
def charts():
    return render_template('charts.html',title="Charts")

@app.route("/login")
def login():  
    return render_template('login.html', title="")

@app.route("/survey")
def survey():
    form=ConfirmationForm()
    choices=[(option.project_name, option.project_name) for option in Projects.query.all()]
    form.project_name.choices=choices

    return render_template("survey.html" ,form=form, title="Project Code Survey")

@app.route("/tentative")
def tentative():
    return render_template('tentative.html',title="Tentative Projects")

@app.route("/snapshot")
def snapshot():
    results=Projects.query.all()
    return render_template('snapshot.html',title="Snapshot",results=results)


@app.route("/stats")
def stats():
    return render_template('stats.html',title="Stats")

if __name__=="__main__":
    app.run(debug=True)
    
  



