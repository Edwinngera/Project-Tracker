from flask_login import login_required,login_manager
from flask import flash,redirect
from models import User



class LoginHander():
    @login_manager.user_loader
    def load_user(user_id):
        """Check if user is logged-in on every page load."""
        if user_id is not None:
            return User.query.get(user_id)
        return None


    @login_manager.unauthorized_handler
    def unauthorized():
        """Redirect unauthorized users to Login page."""
        flash('You must be logged in to view that page.')
        return redirect('/login')