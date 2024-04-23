import csv
from datetime import datetime, timedelta

csv_file = 'data/AvailableRooms.csv'


def read_info():
    """
    Programmer: Vaishnavi Sen

    Date:

    Purpose: Function to read the information from "AvailableRooms.csv"  

    Returns:
        csv_data: List of the information read from csv file. 
    """
    csv_data = []
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        csv_data = list(csv_reader)
    return csv_data

# check for the availability of the rooms
def find_available_room_types(start_date, end_date):
    """
    Programmer: Vaishnavi Sen

    Date:
    
    Purpose: Function to find all the available rooms in the database for given dateset 

    Args:
        start_date: Start date of the reservation.
        end_date: End date of the reservation. 

    Returns:
        available_rooms: An array containing the types of all the available rooms. 
    """
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

# this code is temporary - might be removed while refactoring the above method 
def find_room_number(start_date, end_date, room_type):
    """
    Programmer: Vaishnavi Sen

    Date:
    
    Purpose: Function that returns the room number allocated for a particular reservation.  

    Args:
        start_date: Start date of the reservation.
        end_date: End date of the reservation.
        room_type: Type of the room selected for the reservation. 

    Returns:
        int: Room number allocated for the given reservation. 
    """
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
        
    
        

        