from email.policy import default
import imp
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash

db=SQLAlchemy()


class Projects(db.Model):
    __tablename__='Projects'
    id = db.Column(db.String, primary_key=True, nullable=False)
    project_id=db.Column(db.String, nullable=False)
    project_name = db.Column(db.String, nullable=False)
    client_name=db.Column(db.String, nullable=True)
    client_code=db.Column(db.String, nullable=True)
    curr_end_date=db.Column(db.String, nullable=True)
    curr_end_date=db.Column(db.String, nullable=True)
    engagement_type=db.Column(db.String, nullable=True)
    signing_entity=db.Column(db.String, nullable=True)
    business_entity=db.Column(db.String, nullable=True)
    engagement_number=db.Column(db.String, nullable=True)
    country_one=db.Column(db.String, nullable=True)
    country_two=db.Column(db.String,nullable=True)
    city=db.Column(db.String, nullable=True)
    capability=db.Column(db.String, nullable=True)
    capability1=db.Column(db.String,nullable=True)
    capability3=db.Column(db.String,nullable=True)

    def __repr__(self):
        return f"<Projects id={self.id} project_id={self.project_id} project_name={self.project_name} curr_end_date={self.curr_end_date} >\n"

class Tentative_Projects(db.Model):
    __tablename__="Tentative_Projects"
    id=db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.String,nullable=False)
    project_name=db.Column(db.String,nullable=False)
    project_start_date=db.Column(db.String, nullable=False)
    project_end_date=db.Column(db.String, nullable=False)
    project_type=db.Column(db.String, nullable=False)
    client=db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Tentative_Projects project_name={self.project_name} client={self.client} project_start_date={self.project_start_date} >"

 
class Salesforce(db.Model):
    __tablename__="Salesforce"
    id=db.Column(db.Integer, primary_key=True)
    Opp_Name=db.Column(db.String,nullable=False)
    Salesforce_ID=db.Column(db.String,nullable=False)
    Stage=db.Column(db.String,nullable=False) 

    def __repr__(self):
        return f"<Salesforce Opp_Name={self.Opp_Name} Salesforce_ID={self.Salesforce_ID}  stage={self.Stage}"


    

class Client(db.Model):
    __tablename__="Client"
    id=db.Column(db.Integer,primary_key=True)
    client_code=db.Column(db.Integer,nullable=True)
    client_name=db.Column(db.String, nullable=True)
    
    def __repr__(self):
        
        return f"<Client>"


class Dummy_Projects(db.Model):
    __tablename__='Dummy'
    id = db.Column(db.String, primary_key=True, nullable=False,)
    project_id=db.Column(db.String, nullable=False)
    project_name = db.Column(db.String, nullable=False)
    client_name=db.Column(db.String, nullable=True)
    client_code=db.Column(db.String, nullable=True)
    curr_end_date=db.Column(db.String, nullable=True)
    curr_end_date=db.Column(db.String, nullable=True)
    engagement_type=db.Column(db.String, nullable=True)
    signing_entity=db.Column(db.String, nullable=True)
    business_entity=db.Column(db.String, nullable=True)
    engagement_number=db.Column(db.String, nullable=True)
    country_one=db.Column(db.String, nullable=False)
    country_two=db.Column(db.String,nullable=True)
    city=db.Column(db.String, nullable=True)
    capability=db.Column(db.String, nullable=True)
    capability1=db.Column(db.String,nullable=True)
    capability3=db.Column(db.String,nullable=True)

    def __repr__(self):
        return f"<Projects id={self.id} project_id={self.project_id} project_name={self.project_name} curr_end_date={self.curr_end_date} >\n"


class User(UserMixin, db.Model):
    __tablename__ = "flasklogin-users"
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100), nullable=False)
    email=db.Column(db.String(),nullable=False)
    password=db.Column(db.String(200),nullable=False,unique=False)
    created_on=db.Column(db.DateTime,index=False,unique=False,nullable=True)
    last_login=db.Column(db.DateTime,index=False,unique=False)
    
    
    def set_password(self,password):
        self.password=generate_password_hash(password,method="sha256")
        
    def check_password(self,password):
        return check_password_hash(self.password,password)
    
    def __repr__(self):
        return  '<User {}>'.format(self.username)
        

    
    
    
    





















   
