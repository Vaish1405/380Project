from flask import Flask, render_template, request
import csv

app = Flask(__name__)

CSV_FILE = 'AvailableRooms.csv'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/food')
def food():
    return render_template('food.html')

@app.route('/rooms')
def rooms():
    return render_template('rooms.html')

@app.route('/selectRoom')
def selectRoom():
    return render_template('selectroom.html')

@app.route('/available-rooms')
def availableRooms():
    return f"rooms available"

if __name__ == '__main__':
    app.run(debug=True)