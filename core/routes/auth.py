from flask import (
    Blueprint, 
    request, 
    flash, 
    redirect, 
    url_for, 
    render_template, 
    flash
)
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user

from ..extensions import db
from ..models import User

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        password_check = request.form.get('password_check')

        email_exists = bool(User.query.filter_by(email=email)\
                    .first())

        print(email_exists)

        if password != password_check:
            flash("Passwords do not match")
            return redirect(url_for('auth.register'))
        elif len(password) < 6 or len(password) > 20:
            flash("Password must be between six and twenty characters long.")
            return redirect(url_for('auth.register'))
        elif email_exists:
            flash("Email already in use", "error")
            return redirect(url_for('auth.register'))
        else:
            user = User(
                email=email,
                password_hash=generate_password_hash(password)
            )
            db.session.add(user)
            db.session.commit()
        return redirect(url_for('auth.create_profile'))
    return "register"


@auth.route('/create-profile/', methods=['GET', 'POST'])
def create_profile():
    return "create profile"


@auth.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password_hash, password):
                login_user(user)
                flash("Logged in", "Success")
                return redirect(url_for('auth.profile', 
                                        user_id=user.id
                                    ))
            else: 
                flash("Invalid Credentials!", "Error")
                return redirect(url_for('auth.login'))
        else:
            flash("User does not exist.", "Error")
            return redirect(url_for('auth.login'))
    return render_template('auth/login.html')


@auth.route('/logout/', methods=['GET', 'POST'])
def logout():
    logout_user()
    flash("You have been logged out.")
    return "Logged Out"

@auth.route('/profile/<user_id>', methods=['GET'])
def profile(user_id):
    context = {
        'title' : f"{current_user.name}'s Profile Page",
        'user'  : current_user,
    }
    return f'Hello, {current_user.name}'


@auth.route('/change-password/', methods=['GET', 'POST'])
def change_password():
    return "Change Password"

