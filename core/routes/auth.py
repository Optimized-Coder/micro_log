import datetime
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
from flask_login import login_user, logout_user, current_user, login_required

import re

from ..extensions import db
from ..models import User
from ..functions import validate_password

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/register/', methods=['GET', 'POST'])
def register():
    # TODO:
    # ADD EMAIL CONFIRMATION

    if request.method == 'POST':
        email = request.form.get('email').lower()
        password = request.form.get('password')
        password_confirmation = request.form.get('password_confirmation')

        is_validated = False
        email_exists = bool(User.query.filter_by(email=email).first())
        password_valid = validate_password(password=password,
                                           password_confirmation=password_confirmation)

        # email validation
        if email_exists:
            is_validated = False
            print('Email in use. If you already have an account, please login', 'error')
        elif len(email) < 5:
            is_validated = False
            print('Please enter a valid email address', 'error')
        # password validation
        elif not password_valid:
            is_validated = False
            print('Please enter a valid password', 'error')

        else:
            is_validated = True

        if is_validated:
            print("User is valid")
            usr = User(
                email=email,
                password_hash=generate_password_hash(password, method='sha256')
            )

            db.session.add(usr)
            db.session.commit()
            print('Account Created Successfully', 'success')
            return f"Created user {usr}"

    return "Register"


@auth.route('/create-profile/', methods=['GET', 'POST'])
@login_required
def create_profile():
    ''''
    Function: add more info to a new user's profile, 
    commits to db
    form inputs: ename, height, weight, DoB, gender
    '''
    if request.method == 'POST':
        name = request.form.get('name')
        height_cm = request.form.get('height_cm')
        weight_kg = request.form.get('weight_kg')
        dob_day = request.form.get('day')
        dob_month = request.form.get('month')
        dob_year = request.form.get('year')
        gender = request.form.get('gender')

        user = current_user

        user.name = name
        user.height_cm = height_cm
        user.weight_kg = weight_kg
        user.date_of_birth = datetime.date(int(dob_year), int(dob_month), int(dob_day))
        user.gender = gender

        db.session.commit()
        return (
            f'''
            Name: {user.name}
            Height: {user.height_cm}cm
            Date of Birth: {user.date_of_birth}
            Weight: {user.weight_kg}kg
            Gender: {user.gender}
            '''
        )
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
                return redirect(url_for('main.index'))
            else:
                flash("Invalid Credentials!", "Error")
                return "Invalid Credentials"
        else:
            flash("User does not exist.", "Error")
            return redirect(url_for('auth.login'))
    return render_template('auth/login.html')


@auth.route('/logout/', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return "Logged Out"


@auth.route('/profile/', methods=['GET'])
@login_required
def profile():
    context = {
        'title': f"{current_user.name}'s Profile Page",
        'user': current_user,
    }
    return f'Hello, {current_user.name}'


@auth.route('/change-password/', methods=['GET', 'PUT'])
@login_required
def change_password():
    if request.method == 'PUT':
        old_password = request.form.get('old_password')
        new_password = request.form.get('new_password')
        password_confirmation = request.form.get('password_confirmation')

        user_password = current_user.password_hash

        if check_password_hash(user_password, old_password):
            if old_password == password_confirmation:
                current_user.password_hash = generate_password_hash(new_password)
                db.session.commit()
                flash("Password Changed", "Success")
                return 'Password Changed'
            else:
                flash("Passwords do not match", "Error")
                return 'Try again'
        else:
            flash("Old Password is incorrect", "Error")
            return 'Try again'

        
            
