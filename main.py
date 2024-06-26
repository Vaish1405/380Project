from flask import Flask, render_template, request, session, flash, redirect, jsonify
import stripe, os
import logging
from utility import find_available_room_types, find_room_number
from utility import check_validity, get_total, getDays 
from Rooms import get_room_price
from Extras import get_extras_price
from datetime import datetime
from Reservation import ReservationController, find_reservation
import bcrypt
from utility import upload_user, find_user, hash_password, check_password, find_current_reservation

available_room_types = [] # to store the values read from csv file

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
app.secret_key = os.getenv('app_secret_key')
stripe.api_key = os.getenv('stripe_api_key')
google_maps_api_key = os.getenv('google_maps_api_key')

@app.route('/')
def home():
    session.clear()
    return render_template('index.html', api_key=google_maps_api_key)

@app.route('/food')
def food():
    return render_template('food.html')

@app.route('/rooms')
def rooms():
    return render_template('rooms.html')

@app.route('/dateSelection')
def dateSelection(): 
    return render_template('dateSelection.html')

@app.route('/room-selection', methods=['POST'])
def roomSelection():
    session['check_in'] = request.form.get('check-in')
    session['check_out'] = request.form.get('check-out')
    session['people'] = request.form.get('people')
    result = check_validity(session['check_in'], session['check_out'], session['people'])
    if not result.startswith('Welcome'):
        flash(result) 
        return redirect(request.referrer)
    return render_template('room-selection.html', available_rooms=find_available_room_types(session['check_in'], session['check_out']), form=request.form)
    
@app.route('/extraSelection', methods=['POST', 'GET'])
def extraSelection(): 
    session['room-type'] = request.form.get('select-room')
    return render_template('extraSelection.html', check_in=session['check_in'], 
                           check_out=session['check_out'], people=session['people'])

@app.route('/payment', methods=['POST'])
def payment():
    nights = getDays(session['check_in'], session['check_out'])
    session['extras'] = request.form.get('select-extras')
    return render_template('payment.html', check_in=session['check_in'], 
                           check_out=session['check_out'], people=session['people'], 
                           room_selection=session['room-type'], extras_selection=session['extras'], 
                           roomCost=get_room_price(session['room-type']), 
                           extrasCost=get_extras_price(session['extras']), 
                           nights=nights,
                           total=get_total(nights, session['room-type'], session['extras']),
                           public_key=os.getenv('stripe_public_key'))

@app.route('/create-payment-intent', methods=['POST'])
def create_payment_intent():
    data = request.json
    amount = data['amount']
    currency = data['currency']

    intent = stripe.PaymentIntent.create(
        amount=amount,
        currency=currency
    )
    return jsonify({'clientSecret': intent.client_secret})

@app.route('/roomInfo', methods=['GET'])
def roomInfo():
    return render_template('room-info.html')

@app.route('/amenities')
def amenities():
    return render_template('amenities.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/userSignedUp', methods=['POST', 'GET'])
def userSignedUp():    
    if find_user(request.form.get('email')) == None: 
        session['first-name'] = request.form.get('firstName') or "Guest"
        session["last-name"] = request.form.get('lastName') or " "
        session['name'] = request.form.get('firstName') + ' ' + request.form.get('lastName') 
        session['email'] = request.form.get('email')
        if request.form.get('phone'):
            session['phone'] = request.form.get('phone')
        else: 
            session['phone'] = "Enter your phone number"
        session['password'] = hash_password(request.form.get('password'))
        upload_user(session['name'], session['email'], session['phone'], session['password'])
        return render_template('user.html', user_first_name=session['first-name'], user_last_name=session["last-name"], user_email=session['email'], user_phone=session['phone'])
    else: 
        flash("User already exists!", 'signUp_error')
        return redirect(request.referrer)

@app.route('/userLoggedIn', methods=['POST', 'GET'])
def userLoggedIn():
    if request.referrer == "http://127.0.0.1:5000/signUp":
        session['email'] = request.form.get('email')
        user = find_user(session['email'])
        if user == None:
            flash("User does not exist. Sign up if new user!", 'login_error')
            return redirect(request.referrer)        
        elif check_password(request.form.get('password'), user.password) == False:
            flash("Entered Password is wrong!", 'login_error')
            return redirect(request.referrer)
        else:
            session['first-name'] = user.user_name.split()[0]
            session['last-name'] = user.user_name.split()[1]
            session['name'] = user.user_name
            session['phone'] = user.phone
            return render_template('user.html', user_first_name=session['first-name'], user_last_name=session["last-name"], user_email=session['email'], user_phone=session['phone'])
    
    else:
        return render_template('user.html', user_first_name=session['first-name'], user_last_name=session["last-name"], user_email=session['email'], user_phone=session['phone'])

@app.route('/user', methods=['GET', 'POST'])
def user():
    if request.referrer == "http://127.0.0.1:5000/payment":
        session['first-name'] = request.form.get('first-name')
        session["last-name"] = request.form.get('last-name')
        session['name'] = request.form.get('first-name') + ' ' + request.form.get('last-name')
        session['email'] = request.form.get('email')
        session['room_number'] = find_room_number(session['check_in'], session['check_out'], session['room-type'])   
        reservation = [session['name'], session['check_in'], session['check_out'], session['room-type'], session['room_number']]
        reservation_status = ReservationController(reservation=reservation).make_reservation()
    # if session['first-name']:
    return render_template('user.html', user_first_name=session['first-name'], user_last_name=session["last-name"], 
                               user_email=session['email'])

@app.route('/userReservation')
def userReservation():
    if find_user(session['email']) == None: 
        data = ["", "", session['check_in'], session['check_out'], session['room-type'], session['room_number']]
        return render_template('userReservation.html', current_reservation=data, user_name=session['name'], guest=True)

    data=find_current_reservation(session['name'])
    if data.empty:
        flash("No Reservation found for the current user", 'no_reservation_error')
        return render_template("userReservation.html", user_name=session['name'])  
    else: 
        data = data.values[0]
        session['check_in'] = data[2]
        session['check_out'] = data[3]
        session['room-type'] = data[4]
        session['room_number'] = data[5]
        return render_template('userReservation.html', current_reservation=data, user_name=session['name'])
        
@app.route('/settings')
def settings():
    return render_template('settings.html', user_first_name=session['first-name'], user_last_name=session['last-name'], user_email=session['email'])

@app.route('/editReservationForm')
def editReservationForm():
    return render_template('editReservation.html')

@app.route('/editReservation', methods=['GET','POST'])
def editReservation():
    reservation = [session['name'], session['check_in'], session['check_out'], session['room-type'], session['room_number']]
    # # print(reservation)

    # session['check_in']=request.form.get('new_check_in') or session['check_in'] 
    # session['check_out']=request.form.get('new_check_out') or session['check_out'] 
    # session['room-type']=request.form.get('new_room_type').lower() or session['room-type']
    ReservationController(reservation=reservation).edit_reservation(find_reservation(session['name'], session['check_in'], session['check_out']), 
                                                                                     new_check_in=request.form.get('new_check_in') or session['check_in'], 
                                                                                     new_check_out=request.form.get('new_check_out') or session['check_out'] , 
                                                                                     new_room_type=request.form.get('new_room_type').lower() or session['room-type'])
    # reservation = ['Vaishnavi Sen', '2024-05-14', '2024-05-16', "Standard", 101]
    # ReservationController(reservation=reservation).edit_reservation(find_reservation('Vaishnavi Sen', '2024-05-14', '2024-05-16'), new_check_in="2024-05-12", new_check_out="2024-05-19")
    # 
    # reservation = [session['name'], session['check_in'], session['check_out'], session['room-type'], session['room_number']]
    # print(reservation)
    # ReservationController(reservation=reservation).edit_reservation(new_check_in=request.form.get('new_check_in') or session['check_in'], 
    #                                                                 new_check_out=request.form.get('new_check_out') or session['check_out'], 
    #                                                                 new_room_type=request.form.get('new_room_type').lower() or session['room-type'])
    flash("Reservation updated!", 'success_message')
    return render_template('userReservation.html')

@app.route('/cancelReservation')
def cancelReservation():
    data = find_current_reservation(session['name'])
    data = data.values[0]
    session['check_in'] = data[2]
    session['check_out'] = data[3]
    session['room-type'] = data[4]
    session['room_number'] = data[5]
    reservation = [session['name'], session['check_in'], session['check_out'], session['room-type'], session['room_number']]
    ReservationController(reservation=reservation).cancel_reservation(find_reservation(session['name'], session['check_in'], session['check_out']))
    flash("Reservation cancelled!", 'no_reservation_error')
    return render_template('userReservation.html', user_name=session['name'])

@app.route('/userPageTemp.html', methods=['POST'])
def userPageTemp():
    reservation = [session['name'], session['check_in'], session['check_out'], session['room-type'], session['room_number']]
    ReservationController(reservation=reservation).edit_reservation(new_check_in=request.form.get('new_check_in') or session['check_in'], 
                                                                    new_check_out=request.form.get('new_check_out') or session['check_out'], 
                                                                    new_room_type=request.form.get('new_room_type').lower() or session['room-type'],
                                                                    new_num_people=request.form.get('new_num_people') or session['people'])
    return render_template('userPageTemp.html', message="success!!")

@app.route('/signUp')
def signUp():
    return render_template('signUp.html')

if __name__ == '__main__':
    app.run(debug=True)
    