from flask import Flask,render_template
from forms import ConfirmationForm
from config import Config

app=Flask(__name__)
app.config.from_object(Config)

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
    return render_template("survey.html" ,form=form, title="Project Code Survey")

@app.route("/tentative")
def tentative():
    return render_template('tentative.html',title="Tentative Projects")

@app.route("/snapshot")
def snapshot():
    return render_template('tentative.html',title="Snapshot")


if __name__=="__main__":
    app.run(debug=True)