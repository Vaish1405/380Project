import csv
from roomsAvailability import read_info, csv_file


class Reservation:
    def __init__(self, user_name, user_id, check_in, check_out, room_type):
        self.user_name = user_name
        self.user_id = user_id
        self.checkIn = check_in
        self.checkOut = check_out
        self.room_type = room_type

# For testing purpose
user_name = "Kaung Khant"
user_id = "kk7304"
check_in = "2024-04-03"
check_out = "2024-04-06"
room_type = "Standard"

# Reservation controller to be called from front-end
class ReservationController:
    # This creates object when called from front-end
    reservation = Reservation(user_name, user_id, check_in, check_out, room_type)
    def make_reservation(reservation):
        # Declaring keys in dictionary that is going to be added to CSV file
        main_key = ['user_name', 'user_id', 'check_in', 'check_out', 'room_type']
        # Using dictionary to add the data to CSV file, let me know if you want alternative way
        with open('reservations.csv', mode='a', newline='') as file:
            data_adding = csv.DictWriter(file, fieldnames= main_key)
            data_adding.writerow({'user_name': user_name,
                             'user_id': user_id,
                             'check_in': check_in,
                             'check_out': check_out,
                             'room_type': room_type})
        print("Reservation is successfully done!")
        # Just to clarify, we are passing Reservation object so we use those attributes inside function. Another alternative way is also possible

        # Not necessary, only for testing
        '''
        print("User name: ", reservation.user_name)
        print("User ID: ", reservation.user_id)
        print("Check-in Date", reservation.checkIn)
        print("Check-out Date", reservation.checkOut)
        print("Room Type: ", reservation.room_type)
        '''

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

