from flask import Flask, render_template, request, session
import logging
from roomsAvailability import find_available_rooms

available_room_types = [] # to store the values read from csv file

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
app.secret_key = "Vaish"

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
    return render_template('room-selection.html', available_rooms=find_available_rooms(), form=request.form)

@app.route('/extraSelection', methods=['POST'])
def extraSelection(): 
    session['select-room'] = request.form.get('select-room')
    return render_template('extraSelection.html', info=session)

@app.route('/payment', methods=['POST'])
def payment():
    session['select-extras'] = request.form.get('select-extras')
    return render_template('payment.html', info=session)

@app.route('/selectRoom')
def selectRoom():
    return render_template('selectroom.html')


if __name__ == '__main__':
    app.run(debug=True)