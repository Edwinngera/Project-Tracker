from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
import datetime



class ConfirmationForm(FlaskForm):
    salesforce =SelectField ("Salesforce Opportunity", validators=[DataRequired()], choices=[
            ('Ludique Works - Analyst support (TTA)', 'Ludique Works - Analyst support (TTA)'),
            ('Corrupt Politician', 'politician'),
            ('No-nonsense City Cop', 'cop'),
            ('Professional Rocket League Player', 'rocket'),
            ('Lonely Guy At A Diner', 'lonely'),
            ('Pokemon Trainer', 'pokemon')
        ])
    
    stage =SelectField ("Stage", validators=[DataRequired()], choices=[
            ('Closed Won', 'Closed Won')
        ])


    project_name =SelectField ("Project Name", validators=[DataRequired()], choices=[
            ('MFA', 'MFA')
        ])

    larger_project=SelectField ("Is it part of a larger project?", validators=[DataRequired()], choices=[
            ('Yes', 'Yes')
        ])

    client_type=SelectField ("Client type", validators=[DataRequired()], choices=[
            ('Yes', 'Yes')
        ])


    engagement_type=SelectField ("Engagement Type", validators=[DataRequired()], choices=[
            ('Yes', 'Yes')
        ])

    contract_entity=SelectField ("OCA entity involved in signing the contract", validators=[DataRequired()], choices=[
            ('Yes', 'Yes')
        ])

    cap_raise=SelectField ("Does it include a capital raise component", validators=[DataRequired()], choices=[
            ('Yes', 'Yes'),
             ('No', 'No'),
        ])

    country_of_operation1=SelectField ("Client's main country of operation", validators=[DataRequired()], choices=[
            ('Yes', 'Yes'),
             ('No', 'No'),
        ])

    country_of_operation2=SelectField ("Client's secondary country of operations", validators=[DataRequired()], choices=[
            ('Yes', 'Yes'),
             ('No', 'No'),
        ])

    rural=SelectField ("Is the business located in a rural location or buy/sell in rural areas?", validators=[DataRequired()], choices=[
            ('Yes', 'Yes'),
             ('No', 'No'),
        ])
        


    industry=SelectField ("Industry", validators=[DataRequired()], choices=[
            ('Yes', 'Yes'),
             ('No', 'No'),
        ])

    
    sec_industry=SelectField ("Secondary Industry", validators=[DataRequired()], choices=[
            ('Yes', 'Yes'),
             ('No', 'No'),
        ])


    business_unit=SelectField ("Business unit*", validators=[DataRequired()], choices=[
            ('O', 'O'),
             ('A', 'A'),
             ('AP', 'AP'),
        ])

    client_name=StringField ("Client Name", validators=[DataRequired()])

    startdate = DateField('Start Date', format='%Y-%m-%d')
    enddate = DateField('End Date', format='%Y-%m-%d')

        



    


    
    

    






    

    

    

    

    



    





    password = PasswordField("Password", validators=[DataRequired(),Length(min=6,max=15)])
    password_confirm = PasswordField("Confirm Password", validators=[DataRequired(),Length(min=6,max=15), EqualTo('password')])
    first_name = StringField("First Name", validators=[DataRequired(),Length(min=2,max=55)])
    last_name = StringField("Last Name", validators=[DataRequired(),Length(min=2,max=55)])
    submit = SubmitField("Register Now")
    
