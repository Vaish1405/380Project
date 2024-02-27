from flask import Flask, render_template, request
import csv

csv_file = 'AvailableRooms.csv'

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

@app.route('/available-rooms')
def availableRooms():
    with open(csv_file, 'r') as file:
        available_rooms = csv.DictReader(file)
        for row in available_rooms:
            if row['Available'] == 'True':
                print(f"{row['RoomNumber']}")

    return render_template('temp.html')

if __name__ == '__main__':
    app.run(debug=True)