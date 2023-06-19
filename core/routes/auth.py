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
from ..functions import register_user

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user=register_user()
        
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.create_profile'))
    return "register"


@auth.route('/create-profile/', methods=['GET', 'POST'])
def create_profile():
    if request.method == 'POST':
        name = request.form.get('name')
        height_cm = request.form.get('height_cm')
        weight_kg = request.form.get('weight_kg')
        date_of_birth = request.form.get('date_of_birth')
        gender = request.form.get('gender')

        user = current_user

        user.name = name
        user.height_cm = height_cm
        user.weight_kg = weight_kg
        user.date_of_birth = date_of_birth
        user.gender = gender

        db.session.commit()
        return f"User: {user.name} created"
    return "create_profile"



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
        'title': f"{current_user.name}'s Profile Page",
        'user': current_user,
    }
    return f'Hello, {current_user.name}'


@auth.route('/change-password/', methods=['GET', 'POST'])
def change_password():
    return "Change Password"
