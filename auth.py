from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user
import queue
from main import User
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first() # searches data base for existing user using email
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('/'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required #keeps user from going to page unless logged in, 
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName') # wont work because the field isnt in the HTML
        phone_number = request.form.get('phoneNumber')  # wont work because the field isnt in the HTML
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user_reservations = queue.Queue() # queue to store reservations for each user

        user = User.query.filter_by(email=email).first()
        if user:                                            #makes sure the user isnt already in the DB via email
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif len(last_name) < 2:
            flash('Last name must be greater than 1 character.', category='error')
        elif len(phone_number) != 10 or len(phone_number) != 0: # should make the phone number optional or if included, the correct legth
            flash('Invalid phone number', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email,
                            first_name=first_name,
                            last_name=last_name, 
                            name = first_name + ' ' + last_name, 
                            phone_number = phone_number, 
                            password=generate_password_hash(password1),
                            user_reservatons = user_reservations)
            
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True) # logs in user and remember = true keeps them logged in
            flash('Account created!', category='success') # flash flashes a pop up message on screen
            return redirect(url_for('/')) #takes user to home page after sign up

    return render_template("sign_up.html", user=current_user)
