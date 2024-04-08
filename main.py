from flask import Flask, render_template, request, session, flash, redirect, jsonify
import stripe, os
import logging
from roomsAvailability import find_available_rooms
from ValidateAvailabilityInput import check_validity 
from room_cost import get_room_price
from extras_cost import get_extras_price
from datetime import datetime, timedelta
from reservation import make_reservation, ReservationController
from roomsAvailability import read_info
import csv


def getDays(checkIn, checkOut):
    checkIn = datetime.strptime(checkIn, "%Y-%m-%d")
    checkOut = datetime.strptime(checkOut, "%Y-%m-%d")

    nights = (checkOut - checkIn).days 
    return nights

def get_total(nights, room_selection, extras_selection):
    sum = 0
    sum += int(get_room_price(room_selection)) * int(nights)
    sum += int(get_extras_price(extras_selection))
    sum += 50
    return sum                      

available_room_types = [] # to store the values read from csv file

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
app.secret_key = os.getenv('app_secret_key')
stripe.api_key = os.getenv('stripe_api_key')

@app.route('/')
def home():
    return render_template('index.html')

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
    return render_template('room-selection.html', available_rooms=find_available_rooms(session['check_in'], session['check_out']), form=request.form)
    
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


@app.route('/temp', methods=['POST', 'GET'])
def temp():
    session['name'] = request.form.get('first-name') + ' ' + request.form.get('last-name')
    reservation = [session['name'], session['check_in'], session['check_out'], session['room-type']]
    return render_template('temp.html', temp=ReservationController(reservation=reservation), name=session['name'], check_in=session['check_in'], 
                           check_out=session['check_out'], people=session['people'], 
                           room_selection=session['room-type'], extras_selection=session['extras'])

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

@app.route('/user')
def user():
    return render_template('user.html')

if __name__ == '__main__':
    app.run(debug=True)