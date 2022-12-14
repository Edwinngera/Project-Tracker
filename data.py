from models import *
from flask import jsonify
import json
from dotenv import load_dotenv
import os
import requests
from requests.auth import HTTPBasicAuth


class DashboardData:
    def get_sectors(db):
        sectors_info = []
        sectors = [
            "SME",
            "Gen Eng",
            "Biz Dev",
            "Corporate",
            "Government",
            "Investor",
            "NGO",
        ]
        # sectors=["Agribusiness","Agroforestry","Consumer goods","Education & Workforce development",
        #         "Energy Access","Financial Services","Manufacturing","Political foundation","Technology",
        #         "Trade & Logistics","Water & Sanitation","Other"]
        for x in sectors:
            print(x)
            engagementy_type = (
                db.session.query(Projects)
                .filter(Projects.business_entity.ilike(f"%{x}%"))
                .all()
            )

            sectors_info.append(len(engagementy_type))

        total = sum(sectors_info)

        percentages = {
            sectors[i]: int((sectors_info[i] / total) * 100)
            for i in range(len(sectors))
        }
        res = {sectors[i]: sectors_info[i] for i in range(len(sectors))}

        return res, percentages

    def get_yearly_engagement_count(db):

        years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2021, 2022]
        yearly_projects = []

        for year in years:
            num_projects = (
                db.session.query(Projects)
                .filter(Projects.curr_end_date.ilike(f"%{year}%"))
                .all()
            )
            yearly_projects.append(len(num_projects))

        return yearly_projects

    def get_10k_tentative_projects():
        load_dotenv()
        tentative={}
        API_KEY = os.getenv("API_KEY")
        API_URL = os.getenv("URL")
        headers = {"auth": API_URL}
        auth = HTTPBasicAuth("apikey", API_KEY)
        
        url="https://api.rm.smartsheet.com/api/v1/projects?fields=children&with_archived=false&per_page=250000" 

        params = {"method": "GET", "contentType": "application/json", "auth": API_KEY}

        response = requests.get(
            url, headers=params
        )
        a=response.json()
        
        for i in a["data"]:
            print(i["id"])
            # if i["project_state"]=="Tentative" and i["name"]!=None:
            #     tentative[i["id"]]  =tentative[i["name"]] 
            #     print(tentative) 
              
            
                
            
                
            
        
print(DashboardData.get_10k_tentative_projects())
