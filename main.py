from flask import Flask, render_template, request
from roomsAvailability import find_available_rooms

available_room_types = [] # to store the values read from csv file

app = Flask(__name__)
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

@app.route('/room-selection', methods=['GET'])
def roomSelection():    
    return render_template('room-selection.html', available_rooms=find_available_rooms())

@app.route('/extraSelection')
def extraSelection(): 
    return render_template('extraSelection.html')

if __name__ == '__main__':
    app.run(debug=True)