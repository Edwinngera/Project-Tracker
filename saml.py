from flask import Flask,url_for
from flask_saml2 import ServiceProvider

class TrackerServiceProvider(ServiceProvider):
    
    def get_default_login_return_url():
        return url_for('index')
    
    