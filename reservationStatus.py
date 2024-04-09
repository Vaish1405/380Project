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
