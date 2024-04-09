import csv
from roomsAvailability import read_info, csv_file
from datetime import datetime, timedelta

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
        self.change_availability()

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
        
