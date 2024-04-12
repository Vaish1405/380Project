import csv
from reservation import change_availability
import pandas as pd

# Removing the reservation from csv file after canceling, using pandas
def cancel_reservation(user_name):
    # Reading the data from CSV file using pandas
    read_data = pd.read_csv('reservations.csv')

    # Removing te canceled reservation from csv file
    remove_cancellation = read_data[read_data['user_name'] != user_name]

    # Updating data to CSV file after removing reservation that got canceled
    remove_cancellation.to_csv('reservations.csv', index=False)

# Editing the reservation according to user preference and User ID is unique key
def edit_reservation(user_name, **changes):

    # Defining the data we could change according to the user's preference
    change_data = ['room_type', 'check_in', 'check_out']

    # Reading the data in the CSV file
    with open('reservations.csv', 'r') as file:
        data_reader = csv.DictReader(file)
        read_data = list(data_reader)

        # Editing the reservation by tracking the username in csv file
        for reservation in read_data:
            if reservation['user_name'] == user_name:

                # Editing all possible according to customer's preferences
                for main_key, data in changes.items():
                    if main_key in change_data:
                        reservation[main_key] = data

        # Adding the edited data back to CSV file
        with open('reservations.csv', 'w') as file:
            writer = csv.DictWriter(file, fieldnames=['user_name','check_in', 'check_out', 'room_type'])
            writer.writeheader()
            writer.writerows(read_data)

        # Updating room availability based on the reservation changes
        if 'room_type' in changes:
           change_availability(changes['room_type'])

        return "Your reservation has been updated successfully!"

