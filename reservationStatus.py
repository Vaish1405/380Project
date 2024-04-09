import csv
from reservation import Reservation, change_availability
import pandas as pd

# Removing the reservation from csv file after canceling
def cancel_reservation(user_name):
    # Reading the data from CSV file using pandas
    read_data = pd.read_csv('reservations.csv')

    # Removing te canceled reservation from
    remove_cancellation = read_data[read_data['user_name'] != user_name]

    # Updating data to CSV file after removing reservation that got canceled
    remove_cancellation.to_csv('reservations.csv', index=False)


# Function to retrieve a reservation by user_id
def get_reservation_by_user_id(user_id):
    # Read reservations from the CSV file
    with open('reservations.csv', 'r') as file:
        data_reader = csv.DictReader(file)
        # Iterate through each reservation
        for row in data_reader:
            # Checking if the user_id matches the data
            if row['user_id'] == user_id:
                return Reservation(row['user_id'], row['user_name'], row['check_in'], row['check_out'], row['room_type'])
    # Return None if the reservation for specific User ID is not found
    return None


def edit_reservation(reservation, user_id, **kwargs):
    """
     user_name must be included for each reservation changes for each customer in the database
     Using **kwargs which is flexible for variable number of keyword arguments which are the changes to be made
     Examples would be all possible options check_in, check_out and room_type
   """

    reservation = get_reservation_by_user_id(user_id)

    # We can add validation check if the reservation is found or not

    # Defining the data we could change according to the user's preference
    change_data = ['user_name', 'room_type', 'check_in', 'check_out']

    for key, value in kwargs.items():
        if key in change_data:
            # Updating the attribute of the reservation in data
            setattr(reservation, key, value)

    # Reading the data in the CSV file
    with open('reservations.csv', 'r') as file:
        data_reader = csv.DictReader(file)
        read_data = list(data_reader)

    # Modifying the data back to CSV file
    with open('reservations.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=['user_id','user_name', 'check_in', 'check_out', 'room_type'])
        writer.writeheader()
        for r in read_data:
            # Checking if reservation information by User ID
            if r['user_id'] == user_id:
                # Editing the reservation details for any specific customer
                r['user_name'] = reservation.user_name
                r['room_type'] = reservation.room_type
                r['check_in'] = reservation.check_in
                r['check_out'] = reservation.check_out
            # Changing the data the CSV file according to reservation changes
            writer.writerow(r)

    # Updating room availability based on the reservation changed by customer, essential for specific changes in rooms availability only
    for stored_data, value in kwargs.items():
        if stored_data == 'room type':
            change_availability(reservation.room_type)
    return "Your reservation has been updated successfully!"

'''
cancel_reservation('Kaung Khant')
cancel_reservation('Kaung')
edit_reservation(Reservation,'pz2',room_type='Deluxe')
edit_reservation(Reservation,'as99',room_type='Single', check_in = '2024-04-16')
'''
=======
import csv
from roomsAvailability import read_info, csv_file

# defines the 
class Reservation:
    def __init__(self, user_id, user_name, check_in, check_out, room_type):
        self.user_id = user_id
        self.user_name = user_name
        self.check_in = check_in
        self.check_out = check_out
        self.room_type = room_type

# Adding the reservation to database
def make_reservation(reservation):
    # Declaring keys in dictionary that is going to be added to CSV file
    main_key = ['user_id', 'user_name', 'check_in', 'check_out', 'room_type']
    # Using dictionary to add the data to CSV file, let me know if you want alternative way
    with open('reservations.csv', mode='a', newline='') as file:
        data_adding = csv.DictWriter(file, fieldnames= main_key)
        data_adding.writerow({'user_id' : reservation.user_id,
                            'user_name': reservation.user_name,
                            'check_in': reservation.check_in,
                            'check_out': reservation.check_out,
                            'room_type': reservation.room_type})
    return "successful"

# based on front-end info, it will change room availability after making reservation
def change_availability(self, room_type):
    # Reusing read_info method in roomsAvailability.py to read the data
    read_data = read_info()
    for r in read_data:
        if r['RoomType'] == room_type:
            # This makes available status after reservation is done
            r['Available'] = 'False'
    with open(csv_file, 'w') as file:
        field = ['RoomType', 'Available']
        csv_writer = csv.DictWriter(file, fieldnames=field)
        csv_writer.writerows([r for r in read_data if r['RoomType'] == room_type])

# Reservation controller to be called from front-end
class ReservationController:
    def __init__(self, reservation):
        self.reservation = Reservation(*reservation)
        self.make_reservation()

    def make_reservation(self):
        main_key = ['user_id','user_name', 'check_in', 'check_out', 'room_type']
        # Using dictionary to add the data to CSV file, let me know if you want alternative way
        with open('reservations.csv', mode='a', newline='') as file:
            data_adding = csv.DictWriter(file, fieldnames= main_key)
            data_adding.writerow({'user_id': self.reservation.user_id,
                                'user_name': self.reservation.user_name,
                                'check_in': self.reservation.check_in,
                                'check_out': self.reservation.check_out,
                                'room_type': self.reservation.room_type})
        return self.reservation

'''
reservation_data1 = ('jd1','John Doe', '2024-04-08', '2024-04-10', 'Single')
reservation_controller1 = ReservationController(reservation_data1)

reservation_data2 = ('dc2','David Chan', '2024-04-20', '2024-04-23', 'Deluxe')
reservation_controller2 = ReservationController(reservation_data2)

reservation_data3 = ('at3','Aung Thu', '2024-04-26', '2024-04-28', 'Deluxe')
reservation_controller3 = ReservationController(reservation_data3)

reservation_data4 = ('kk4', 'Kaung Khant', '2024-04-19', '2024-04-22','Deluxe')
reservation_controller4 = ReservationController(reservation_data4)

reservation_data5 = ('pz3','PPZ', '2024-04-19', '2024-04-20','Deluxe')
reservation_controller5 = ReservationController(reservation_data5)
'''
