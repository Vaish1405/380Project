import csv
from roomsAvailability import read_info, csv_file
from datetime import datetime, timedelta
import pandas as pd
import uuid

def find_reservation(user_name, check_in, check_out):
    read_data = pd.read_csv('reservations.csv')
    reservation_data = read_data[(read_data['user_name'] == user_name) & 
                                 (read_data['check_in'] == check_in) & 
                                 (read_data['check_out'] == check_out)]

    return reservation_data

# defines the 
class Reservation:
    def __init__(self, unique_id, user_name, check_in, check_out, room_type):
        self.unique_id = unique_id
        self.user_name = user_name
        self.check_in = check_in
        self.check_out = check_out
        self.room_type = room_type

# Reservation controller to be called from front-end
class ReservationController:
    def __init__(self, reservation):
        self.reservation = Reservation(uuid.uuid4(), *reservation)

    def make_reservation(self):
        self.change_availability('false')
        main_key = ['reservation_id', 'user_name', 'check_in', 'check_out', 'room_type']
        # Adding reservation to the file 
        with open('reservations.csv', mode='a', newline='') as file:
            data_adding = csv.DictWriter(file, fieldnames=main_key)
            data_adding.writerow({
                'reservation_id': self.reservation.unique_id,
                'user_name': self.reservation.user_name,
                'check_in': self.reservation.check_in,
                'check_out': self.reservation.check_out,
                'room_type': self.reservation.room_type
            })
        return self.reservation

    def change_availability(self, value):
        # read data and change the
        with open('AvailableRooms.csv', mode="r") as file:
            read_data = csv.reader(file)
            header = next(read_data)
            rows = []

            for row in read_data:
                if row[1] == self.reservation.room_type:
                    start_date = datetime.strptime(self.reservation.check_in, '%Y-%m-%d')
                    end_date = datetime.strptime(self.reservation.check_out, '%Y-%m-%d')
                    current_date = start_date
                    while current_date <= end_date:
                        row[header.index(current_date.strftime('%Y-%m-%d'))] = value
                        current_date += timedelta(days=1)
                rows.append(row)

        # write the updated data back to the csv file
        with open('AvailableRooms.csv', mode='w') as file:
            write_data = csv.writer(file)
            write_data.writerow(header)
            write_data.writerows(rows)

    # Removing the reservation from csv file after canceling, using pandas
    def cancel_reservation(self, cancel_reservation_id):
        self.change_availability(" true")
        
        # Reading the data from CSV file using pandas
        read_data = pd.read_csv('reservations.csv')


        # Remove the canceled reservation from the DataFrame
        read_data.drop(cancel_reservation_id.index, inplace=True)
        
        # Updating data to CSV file after removing reservation that got canceled
        read_data.to_csv('reservations.csv', index=False)

    # Editing the reservation according to user preference and User ID is unique key
    def edit_reservation(self, **changes):
        self.cancel_reservation(find_reservation(self.reservation.user_name, self.reservation.check_in, self.reservation.check_out))
        for key, val in changes.items(): 
            if key == 'new_check_in':
                self.reservation.check_in = val
            if key == 'new_check_out':
                self.reservation.check_out = val
            if key == 'new_toom_type':
                self.reservation.room_type = val
    
        self.make_reservation()

# reservation = ['Ruben B', '2024-04-12', '2024-04-14', 'Deluxe']
# id = find_reservation('Ruben B', '2024-04-12', '2024-04-14')
# ReservationController(reservation).make_reservation()
# ReservationController(reservation).edit_reservation(new_check_in="2024-04-13")

