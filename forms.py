from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField,validators
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
import datetime
from models import Projects, Salesforce, Tentative_Projects


class ConfirmationForm(FlaskForm):
    salesforce = SelectField("Salesforce Opportunity", validators=[DataRequired()])

    stage = SelectField(
        "Stage", validators=[DataRequired()], choices=[("Closed Won", "Closed Won")]
    )

    # choices=[(option.project_name, option.project_name) for option in Projects.query.all()]
    project_name = SelectField("Project Name", validators=[DataRequired()])
    larger_project = SelectField(
        "Is it part of a larger project?",
        validators=[DataRequired()],
        choices=[(" ", ""), ("Yes", "Yes"), ("No", "No")],
    )

    client_type = SelectField(
        "Client type",
        validators=[DataRequired()],
        choices=[
            (" ", ""),
            ("SME", "SME"),
            ("NGO", "NGO"),
            ("Investor", "Investor"),
            ("Corporate", "Corporate"),
            ("Government", "Government"),
        ],
    )

    engagement_type = SelectField(
        "Engagement Type",
        validators=[DataRequired()],
        choices=[
            (" ", ""),
            ("SME", "SME"),
            ("NGO", "NGO"),
            ("Investor", "Investor"),
            ("Corporate", "Corporate"),
            ("Government", "Government"),
        ],
    )

    contract_entity = SelectField(
        "OCA entity involved in signing the contract",
        validators=[DataRequired()],
        choices=[
            (" ", ""),
            ("General Engagement", "General Engagement"),
            ("SME Engagement", "SME Engagement"),
        ],
    )

    cap_raise = SelectField(
        "Does it include a capital raise component",
        validators=[DataRequired()],
        choices=[
            (" ", ""),
            ("Yes", "Yes"),
            ("No", "No"),
        ],
    )

    country_of_operation1 = SelectField(
        "Client's main country of operation",
        validators=[DataRequired()],
        choices=[
            (" ", ""),
            ("Algeria", "Algeria"),
            ("Angola", "Angola"),
            ("Benin", "Benin"),
            ("Botswana", "Botswana"),
            ("Burundi", "Burundi"),
            ("Cameroon", "Cameroon"),
            ("Cape Verde", "Cape Verde"),
            ("CAR", "CAR"),
            ("Chad", "Chad"),
            ("CAR", "CAR"),
            ("Comoros", "Comoros"),
            ("Congo", "Congo"),
            ("Cote d'Ivoire", "Cote d'Ivoire"),
            ("Djibouti", "Djibouti"),
            ("DRC", "DRC"),
            ("Egypt", "Egypt"),
            ("Equatorial Guinea", "Equatorial Guinea"),
            ("Eritrea", "Eritrea"),
            ("Ethiopia", "Ethiopia"),
            ("Gabon", "Gabon"),
            ("Gambia", "Gambia"),
            ("Ghana", "Ghana"),
            ("Guinea", "Guinea"),
            ("Guinea-Bissau", "Guinea-Bissau"),
            ("Kenya", "Kenya"),
            ("Lesotho", "Lesotho"),
            ("Liberia", "Liberia"),
            ("Libya", "Libya"),
            ("Madagascar", "Madagascar"),
            ("Malawi", "Malawi"),
            ("Mali", "Mali"),
            ("Mauritania", "Mauritania"),
            ("Mauritius", "Mauritius"),
            ("Mayotte", "Mayotte"),
            ("Morocco", "Morocco"),
            ("Mozambique", "Mozambique"),
            ("Namibia", "Namibia"),
            ("Niger", "Niger"),
            ("Nigeria", "Nigeria"),
            ("Other", "Other"),
            ("Réunion", "Réunion"),
            ("Rwanda", "Rwanda"),
            ("Sao Tome and Principe", "Sao Tome and Principe"),
            ("Senegal", "Senegal"),
            ("Sierra Leone", "Sierra Leone"),
            ("Somalia", "Somalia"),
            ("South Africa", "South Africa"),
            ("South Sudan", "South Sudan"),
            ("Southern Africa", "Southern Africa"),
            ("Sudan", "Sudan"),
            ("Swaziland", "Swaziland"),
            ("Tanzania", "Tanzania"),
            ("Togo", "Togo"),
            ("Tunisia", "Tunisia"),
            ("Uganda", "Uganda"),
            ("Western Sahara", "Western Sahara"),
            ("Zambia", "Zambia"),
            ("Zimbabwe", "Zimbabwe"),
        ],
    )

    country_of_operation2 = SelectField(
        "Client's secondary country of operations",
        validators=[DataRequired()],
        choices=[
            ("", ""),
            ("Algeria", "Algeria"),
            ("Angola", "Angola"),
            ("Benin", "Benin"),
            ("Botswana", "Botswana"),
            ("Burundi", "Burundi"),
            ("Cameroon", "Cameroon"),
            ("Cape Verde", "Cape Verde"),
            ("CAR", "CAR"),
            ("Chad", "Chad"),
            ("CAR", "CAR"),
            ("Comoros", "Comoros"),
            ("Congo", "Congo"),
            ("Cote d'Ivoire", "Cote d'Ivoire"),
            ("Djibouti", "Djibouti"),
            ("DRC", "DRC"),
            ("Egypt", "Egypt"),
            ("Equatorial Guinea", "Equatorial Guinea"),
            ("Eritrea", "Eritrea"),
            ("Ethiopia", "Ethiopia"),
            ("Gabon", "Gabon"),
            ("Gambia", "Gambia"),
            ("Ghana", "Ghana"),
            ("Guinea", "Guinea"),
            ("Guinea-Bissau", "Guinea-Bissau"),
            ("Kenya", "Kenya"),
            ("Lesotho", "Lesotho"),
            ("Liberia", "Liberia"),
            ("Libya", "Libya"),
            ("Madagascar", "Madagascar"),
            ("Malawi", "Malawi"),
            ("Mali", "Mali"),
            ("Mauritania", "Mauritania"),
            ("Mauritius", "Mauritius"),
            ("Mayotte", "Mayotte"),
            ("Morocco", "Morocco"),
            ("Mozambique", "Mozambique"),
            ("Namibia", "Namibia"),
            ("Niger", "Niger"),
            ("Nigeria", "Nigeria"),
            ("Other", "Other"),
            ("Réunion", "Réunion"),
            ("Rwanda", "Rwanda"),
            ("Sao Tome and Principe", "Sao Tome and Principe"),
            ("Senegal", "Senegal"),
            ("Sierra Leone", "Sierra Leone"),
            ("Somalia", "Somalia"),
            ("South Africa", "South Africa"),
            ("South Sudan", "South Sudan"),
            ("Southern Africa", "Southern Africa"),
            ("Sudan", "Sudan"),
            ("Swaziland", "Swaziland"),
            ("Tanzania", "Tanzania"),
            ("Togo", "Togo"),
            ("Tunisia", "Tunisia"),
            ("Uganda", "Uganda"),
            ("Western Sahara", "Western Sahara"),
            ("Zambia", "Zambia"),
            ("Zimbabwe", "Zimbabwe"),
        ],
    )

    rural = SelectField(
        "Is the business located in a rural location or buy/sell in rural areas?",
        validators=[DataRequired()],
        choices=[
            (" ", ""),
            ("Yes", "Yes"),
            ("No", "No"),
        ],
    )

    industry = SelectField(
        "Industry",
        validators=[DataRequired()],
        choices=[
            (" ", ""),
            ("Yes", "Yes"),
            ("No", "No"),
        ],
    )

    sec_industry = SelectField(
        "Secondary Industry",
        validators=[DataRequired()],
        choices=[
            (" ", ""),
            ("Yes", "Yes"),
            ("No", "No"),
        ],
    )

    business_unit = SelectField(
        "Business unit*",
        validators=[DataRequired()],
        choices=[
            (" ", ""),
            ("A", "A"),
            ("AP", "AP"),
            ("O", "O"),
        ],
    )

    client_name = StringField("Client Name", validators=[DataRequired()])

    startdate = DateField("Start Date", format="%Y-%m-%d")
    enddate = DateField("End Date", format="%Y-%m-%d")

    # Project Details
    capability1 = StringField("OCA capability 1", validators=[DataRequired()])
    capability2 = StringField("OCA capability 2", validators=[DataRequired()])

    # Practicum details
    primary_support = SelectField(
        "Primary support the analyst will be providing",
        validators=[DataRequired()],
        choices=[
            ("O", "O"),
            ("A", "A"),
            ("AP", "AP"),
        ],
    )

    secondary_support = SelectField(
        "Secondary support the analyst will be providing",
        validators=[DataRequired()],
        choices=[
            ("A", "A"),
            ("AP", "AP"),
            ("O", "O"),
        ],
    )

    city = SelectField(
        "In which city will the analyst be based?",
        validators=[DataRequired()],
        choices=[
            ("O", "O"),
            ("A", "A"),
            ("AP", "AP"),
        ],
    )

    project_summary = StringField(
        "Project summary (1-2 phrases)", validators=[DataRequired()]
    )
    # Key client contact
    full_name = StringField("Full Name", validators=[DataRequired()])
    email = StringField("Email Address", validators=[DataRequired()])

    loe_provided = SelectField(
        "Have you previously provided Budget LOE via the project code survey? [i.e., if part of a larger project]",
        validators=[DataRequired()],
        choices=[
            ("No", "No"),
            ("Yes", "Yes"),
        ],
    )

    partner = StringField("Partner", validators=[DataRequired()])

    associate_partner = StringField("Associate Partner", validators=[DataRequired()])

    principal = StringField("Principal", validators=[DataRequired()])

    spl = StringField("Senior PL / Senior TL", validators=[DataRequired()])

    pl = StringField("Project Leader / Transaction leader", validators=[DataRequired()])

    associate = StringField("(S) Associate", validators=[DataRequired()])

    analyst = StringField("(S) Analyst", validators=[DataRequired()])

    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=6, max=15)]
    )
    password_confirm = PasswordField(
        "Confirm Password",
        validators=[DataRequired(), Length(min=6, max=15), EqualTo("password")],
    )
    first_name = StringField(
        "First Name", validators=[DataRequired(), Length(min=2, max=55)]
    )
    last_name = StringField(
        "Last Name", validators=[DataRequired(), Length(min=2, max=55)]
    )
    submit = SubmitField("Register Now")


class SignupForm(FlaskForm):
    name = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    email = StringField(
        "Email", validators=[DataRequired(), Email(message="Enter a valid email")]
    )
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log In")
