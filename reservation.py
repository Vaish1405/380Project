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

    return reservation_data['reservation_id']

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
        self.make_reservation()
        self.change_availability()

    def make_reservation(self):
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

    def change_availability(self):
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
                        row[header.index(current_date.strftime('%Y-%m-%d'))] = 'false'
                        current_date += timedelta(days=1)
                rows.append(row)

        # write the updated data back to the csv file
        with open('AvailableRooms.csv', mode='w') as file:
            write_data = csv.writer(file)
            write_data.writerow(header)
            write_data.writerows(rows)

    


# print(find_reservation('y Sen', '2024-04-17', '2024-04-25'))