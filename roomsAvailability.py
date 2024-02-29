import csv

csv_file = 'AvailableRooms.csv'

# method to read from csv file and store in the array
def read_info():
    csv_data = []
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        csv_data = list(csv_reader)
    return csv_data

# check for the availability of the rooms
def find_available_rooms():
    available_room_types = []
    data_read = read_info()
    for i in data_read:
        if i['Available'].lower() == 'true' and i['RoomType'] not in available_room_types:
            available_room_types.append(i['RoomType'])

    return available_room_types