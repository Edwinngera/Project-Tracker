from flask import Flask,render_template,redirect,request
from forms import ConfirmationForm,Tentative_Projects,Salesforce
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config





app=Flask(__name__)
app.config.from_object(Config)
from models import db,Projects,Dummy_Projects,Salesforce
db.init_app(app) #Add this line Before migrate line
migrate = Migrate(app, db)



@app.route("/")
def home():
    engagements=Projects.query.all()
    #Kenya
    db_response = db.session.query(Projects).filter(
        Projects.engagement_number.ilike(f'%{"Kenya"}%')
        ).all()
    #Uganda
    uganda=  db.session.query(Projects).filter(
        Projects.engagement_number.ilike(f'%{"Uganda"}%')
        ).all()
    
    kenya=len(db_response)
    return render_template('home.html',title="Dashboard",engagements=len(engagements), kenya=kenya)

@app.route("/charts")
def charts():
    return render_template('charts.html',title="Charts")

@app.route("/login")
def login():  
    return render_template('login.html', title="")

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/survey")
def survey():
    form=ConfirmationForm()
    choices = [("", "---")]
    choices=[(option.project_name, option.project_name) for option in Projects.query.all()]
    salesforce=Salesforce.query.all()
    print(salesforce)
    sf_choices=[(option.Opp_Name, option.Opp_Name) for option in Salesforce.query.all()]
   
    form.project_name.choices=choices
    form.salesforce.choices=sf_choices
    return render_template("survey.html" ,form=form, title="Project Code Survey")

@app.route("/submit-survey", methods=['POST', 'GET'])
def submit_survey():
    form=ConfirmationForm(request.form)
    if form.validate():

        print(form.salesforce.data)
        # dummy_prj=Dummy_Projects(
        #     salesforce=form.salesforce.data,
        #     stage=form.stage.data,
        #     larger_project=form.client_type,
        #     client_type= form.client_type.data,
        #     engagement_type=form.engagement_type.data
        # )
    return redirect('/')


@app.route("/tentative")
def tentative():
    t_projects=Tentative_Projects.query.all()
    return render_template('tentative.html',title="Tentative Projects",results=t_projects)

@app.route("/snapshot")
def snapshot():
    results=Projects.query.all()
    return render_template('snapshot.html',title="Snapshot",results=results)


@app.route("/stats")
def stats():
    return render_template('test.html',title="Stats")

if __name__=="__main__":
    app.run(debug=True)
    
  
