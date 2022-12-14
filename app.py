from flask import Flask, render_template, redirect, request, flash,url_for
from werkzeug.security import generate_password_hash,check_password_hash
from forms import (
    ConfirmationForm,
    Tentative_Projects,
    Salesforce,
    LoginForm,
    SignupForm,
)
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
import json
from data import DashboardData
from flask_login import (
    login_required,
    logout_user,
    current_user,
    login_user,
    LoginManager,
)


login_manager = LoginManager()
app = Flask(__name__)
app.config.from_object(Config)
from models import db, Projects, Dummy_Projects, Salesforce, User

db.init_app(app)
login_manager.init_app(app)

# from auth import LoginHander

migrate = Migrate(app, db)

# with app.app_context():
#     import auth

@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash("You must be logged in to view that page.")
    return redirect("/login")

@app.route("/")
@login_required
def home():
    engagements = Projects.query.all()
    # Kenya
    db_response = (
        db.session.query(Projects).filter(Projects.city.ilike(f'%{"Kenya"}%')).all()
    )
    # Uganda
    uganda = (
        db.session.query(Projects).filter(Projects.city.ilike(f'%{"Uganda"}%')).all()
    )
    nigeria = len(
        db.session.query(Projects).filter(Projects.city.ilike(f'%{"Nigeria"}%')).all()
    )

    kenya = len(db_response)
    uganda = len(uganda)
    user = {"firstname": "Mr.", "lastname": "My Father's Son"}
    output = len(engagements)

    countries = {
        "BD": "Bangladesh",
        "BE": "Belgium",
        "BF": "Burkina Faso",
        "BG": "Bulgaria",
        "BA": "Bosnia and Herzegovina",
        "BB": "Barbados",
        "WF": "Wallis and Futuna",
        "BL": "Saint Barthelemy",
        "BM": "Bermuda",
        "BN": "Brunei",
        "BO": "Bolivia",
        "BH": "Bahrain",
        "BI": "Burundi",
        "BJ": "Benin",
        "BT": "Bhutan",
        "JM": "Jamaica",
        "BV": "Bouvet Island",
        "BW": "Botswana",
        "WS": "Samoa",
        "BQ": "Bonaire, Saint Eustatius and Saba ",
        "BR": "Brazil",
        "BS": "Bahamas",
        "JE": "Jersey",
        "BY": "Belarus",
        "BZ": "Belize",
        "RU": "Russia",
        "RW": "Rwanda",
        "RS": "Serbia",
        "TL": "East Timor",
        "RE": "Reunion",
        "TM": "Turkmenistan",
        "TJ": "Tajikistan",
        "RO": "Romania",
        "TK": "Tokelau",
        "GW": "Guinea-Bissau",
        "GU": "Guam",
        "GT": "Guatemala",
        "GS": "South Georgia and the South Sandwich Islands",
        "GR": "Greece",
        "GQ": "Equatorial Guinea",
        "GP": "Guadeloupe",
        "JP": "Japan",
        "GY": "Guyana",
        "GG": "Guernsey",
        "GF": "French Guiana",
        "GE": "Georgia",
        "GD": "Grenada",
        "GB": "United Kingdom",
        "GA": "Gabon",
        "SV": "El Salvador",
        "GN": "Guinea",
        "GM": "Gambia",
        "GL": "Greenland",
        "GI": "Gibraltar",
        "GH": "Ghana",
        "OM": "Oman",
        "TN": "Tunisia",
        "JO": "Jordan",
        "HR": "Croatia",
        "HT": "Haiti",
        "HU": "Hungary",
        "HK": "Hong Kong",
        "HN": "Honduras",
        "HM": "Heard Island and McDonald Islands",
        "VE": "Venezuela",
        "PR": "Puerto Rico",
        "PS": "Palestinian Territory",
        "PW": "Palau",
        "PT": "Portugal",
        "SJ": "Svalbard and Jan Mayen",
        "PY": "Paraguay",
        "IQ": "Iraq",
        "PA": "Panama",
        "PF": "French Polynesia",
        "PG": "Papua New Guinea",
        "PE": "Peru",
        "PK": "Pakistan",
        "PH": "Philippines",
        "PN": "Pitcairn",
        "PL": "Poland",
        "PM": "Saint Pierre and Miquelon",
        "ZM": "Zambia",
        "EH": "Western Sahara",
        "EE": "Estonia",
        "EG": "Egypt",
        "ZA": "South Africa",
        "EC": "Ecuador",
        "IT": "Italy",
        "VN": "Vietnam",
        "SB": "Solomon Islands",
        "ET": "Ethiopia",
        "SO": "Somalia",
        "ZW": "Zimbabwe",
        "SA": "Saudi Arabia",
        "ES": "Spain",
        "ER": "Eritrea",
        "ME": "Montenegro",
        "MD": "Moldova",
        "MG": "Madagascar",
        "MF": "Saint Martin",
        "MA": "Morocco",
        "MC": "Monaco",
        "UZ": "Uzbekistan",
        "MM": "Myanmar",
        "ML": "Mali",
        "MO": "Macao",
        "MN": "Mongolia",
        "MH": "Marshall Islands",
        "MK": "Macedonia",
        "MU": "Mauritius",
        "MT": "Malta",
        "MW": "Malawi",
        "MV": "Maldives",
        "MQ": "Martinique",
        "MP": "Northern Mariana Islands",
        "MS": "Montserrat",
        "MR": "Mauritania",
        "IM": "Isle of Man",
        "UG": "Uganda",
        "TZ": "Tanzania",
        "MY": "Malaysia",
        "MX": "Mexico",
        "IL": "Israel",
        "FR": "France",
        "IO": "British Indian Ocean Territory",
        "SH": "Saint Helena",
        "FI": "Finland",
        "FJ": "Fiji",
        "FK": "Falkland Islands",
        "FM": "Micronesia",
        "FO": "Faroe Islands",
        "NI": "Nicaragua",
        "NL": "Netherlands",
        "NO": "Norway",
        "NA": "Namibia",
        "VU": "Vanuatu",
        "NC": "New Caledonia",
        "NE": "Niger",
        "NF": "Norfolk Island",
        "NG": "Nigeria",
        "NZ": "New Zealand",
        "NP": "Nepal",
        "NR": "Nauru",
        "NU": "Niue",
        "CK": "Cook Islands",
        "XK": "Kosovo",
        "CI": "Ivory Coast",
        "CH": "Switzerland",
        "CO": "Colombia",
        "CN": "China",
        "CM": "Cameroon",
        "CL": "Chile",
        "CC": "Cocos Islands",
        "CA": "Canada",
        "CG": "Republic of the Congo",
        "CF": "Central African Republic",
        "CD": "Democratic Republic of the Congo",
        "CZ": "Czech Republic",
        "CY": "Cyprus",
        "CX": "Christmas Island",
        "CR": "Costa Rica",
        "CW": "Curacao",
        "CV": "Cape Verde",
        "CU": "Cuba",
        "SZ": "Swaziland",
        "SY": "Syria",
        "SX": "Sint Maarten",
        "KG": "Kyrgyzstan",
        "KE": "Kenya",
        "SS": "South Sudan",
        "SR": "Suriname",
        "KI": "Kiribati",
        "KH": "Cambodia",
        "KN": "Saint Kitts and Nevis",
        "KM": "Comoros",
        "ST": "Sao Tome and Principe",
        "SK": "Slovakia",
        "KR": "South Korea",
        "SI": "Slovenia",
        "KP": "North Korea",
        "KW": "Kuwait",
        "SN": "Senegal",
        "SM": "San Marino",
        "SL": "Sierra Leone",
        "SC": "Seychelles",
        "KZ": "Kazakhstan",
        "KY": "Cayman Islands",
        "SG": "Singapore",
        "SE": "Sweden",
        "SD": "Sudan",
        "DO": "Dominican Republic",
        "DM": "Dominica",
        "DJ": "Djibouti",
        "DK": "Denmark",
        "VG": "British Virgin Islands",
        "DE": "Germany",
        "YE": "Yemen",
        "DZ": "Algeria",
        "US": "United States",
        "UY": "Uruguay",
        "YT": "Mayotte",
        "UM": "United States Minor Outlying Islands",
        "LB": "Lebanon",
        "LC": "Saint Lucia",
        "LA": "Laos",
        "TV": "Tuvalu",
        "TW": "Taiwan",
        "TT": "Trinidad and Tobago",
        "TR": "Turkey",
        "LK": "Sri Lanka",
        "LI": "Liechtenstein",
        "LV": "Latvia",
        "TO": "Tonga",
        "LT": "Lithuania",
        "LU": "Luxembourg",
        "LR": "Liberia",
        "LS": "Lesotho",
        "TH": "Thailand",
        "TF": "French Southern Territories",
        "TG": "Togo",
        "TD": "Chad",
        "TC": "Turks and Caicos Islands",
        "LY": "Libya",
        "VA": "Vatican",
        "VC": "Saint Vincent and the Grenadines",
        "AE": "United Arab Emirates",
        "AD": "Andorra",
        "AG": "Antigua and Barbuda",
        "AF": "Afghanistan",
        "AI": "Anguilla",
        "VI": "U.S. Virgin Islands",
        "IS": "Iceland",
        "IR": "Iran",
        "AM": "Armenia",
        "AL": "Albania",
        "AO": "Angola",
        "AQ": "Antarctica",
        "AS": "American Samoa",
        "AR": "Argentina",
        "AU": "Australia",
        "AT": "Austria",
        "AW": "Aruba",
        "IN": "India",
        "AX": "Aland Islands",
        "AZ": "Azerbaijan",
        "IE": "Ireland",
        "ID": "Indonesia",
        "UA": "Ukraine",
        "QA": "Qatar",
        "MZ": "Mozambique",
    }
    count = 0
    codes = []
    times = []
    for x in countries:
        occurrences = len(
            db.session.query(Projects)
            .filter(Projects.city.ilike(f"%{countries[x]}%"))
            .all()
        )
        codes.append(x)
        times.append(occurrences)
    z = dict(zip(codes, times))

    sector, percentages = DashboardData.get_sectors(db)

    projects_per_year = DashboardData.get_yearly_engagement_count(db)
    print("Edwin")
    print(projects_per_year)
    print(percentages)
    return render_template(
        "home.html",
        title="Dashboard",
        output=output,
        nigeria=nigeria,
        engagements=len(engagements),
        uganda=uganda,
        kenya=kenya,
        countries=z,
        user=user,
        sectors=sector,
        percentages=percentages,
        projects=projects_per_year,
    )

@login_required
@app.route("/charts")
def charts():
    return render_template("charts.html", title="Charts")


@app.route("/login", methods=["POST", "GET"])
def login():
      if current_user.is_authenticated:
        return redirect('/')
      else:
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data).first()
            if user and user.check_password(password=form.password.data):
                login_user(user)
                next_page = request.args.get('next')
                return redirect(next_page or url_for('home'))

            flash('Invalid username/password combination')      
        return render_template("login.html", title="", form=form)


@app.route("/register",methods=["POST", "GET"] )
def register():
    form = SignupForm(request.form)
    if request.method == 'POST' and form.validate():
        print("Ngera")
        existing_user = User.query.filter_by(email=form.email.data).first()
        print(existing_user)
        if existing_user is None:
                user = User(
                    name=form.name.data,
                    email=form.email.data,
                )
                user.set_password(form.password.data)
                db.session.add(user)
                db.session.commit()  # Create new user
                login_user(user)  # Log in as newly created user
                return redirect(url_for('home'))
        # flash('A user already exists with that email address.')
    else:
        print("Invalid")
        return render_template("register.html", form=form)
    
    
@login_required
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route("/survey")
def survey():
    form = ConfirmationForm()
    choices = [("", " ")] + [
        (option.project_name, option.project_name) for option in Projects.query.all()
    ]
    salesforce = Salesforce.query.all()
    print(salesforce)
    sf_choices = [("", " ")] + [
        (option.Opp_Name, option.Opp_Name) for option in Salesforce.query.all()
    ]

    form.project_name.choices = choices
    form.salesforce.choices = sf_choices
    return render_template("survey.html", form=form, title="Project Code Survey")


@app.route("/submit-survey", methods=["POST", "GET"])
def submit_survey():
    form = ConfirmationForm(request.form)
    if form.validate():

        print(form.salesforce.data)
        # dummy_prj=Dummy_Projects(
        #     salesforce=form.salesforce.data,
        #     stage=form.stage.data,
        #     larger_project=form.client_type,
        #     client_type= form.client_type.data,
        #     engagement_type=form.engagement_type.data
        # )
    return redirect("/")


@app.route("/tentative")
def tentative():
    t_projects = Tentative_Projects.query.all()
    return render_template(
        "tentative.html", title="Tentative Projects", results=t_projects
    )


@app.route("/snapshot")
def snapshot():
    results = Projects.query.all()
    return render_template("snapshot.html", title="Snapshot", results=results)


@app.route("/stats")
def stats():
    return render_template("test.html", title="Stats")


@app.route("/admin")
def admin():
    return render_template("admin.html",title="Admin")
    



if __name__ == "__main__":
    app.run(debug=True)
    
