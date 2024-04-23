import csv
from datetime import datetime, timedelta

csv_file = 'data/AvailableRooms.csv'

# method to read from csv file and store in the array
def read_info():
    csv_data = []
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        csv_data = list(csv_reader)
    return csv_data

# check for the availability of the rooms
def find_available_room_types(start_date, end_date):
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    available_rooms = []

    data_read = read_info()

    for room in data_read:
        room_available = True
        current_date = start_date
        while current_date <= end_date:
            if room.get(current_date.strftime("%Y-%m-%d")) != 'true':
                room_available = False
                break
            current_date += timedelta(days=1)  # Move to the next date
        
        # If the room is available for the entire date range, append it to available_rooms
        if room_available and room['RoomType'] not in available_rooms:
            available_rooms.append(room['RoomType'])
    return available_rooms

def find_room_number(start_date, end_date, room_type):
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    data_read = read_info()
    for room in data_read:
        room_available = True
        if room['RoomType'].lower() == room_type.lower():
            current_date = start_date
            while current_date <= end_date:
                if room.get(current_date.strftime("%Y-%m-%d")) != 'true':
                    room_available = False
                    break
                current_date += timedelta(days=1)
        
            if room_available:
                return room['RoomNumber']
        
    
        

        