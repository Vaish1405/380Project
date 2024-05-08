from .Reservation import Reservation
import csv
import uuid
from datetime import datetime, timedelta
from .find_reservation import find_reservation
import pandas as pd
from utility import find_room_number

# Reservation controller to be called from front-end
class ReservationController:
    """
    Programmer: Vaishnavi Sen and Kaung Khant
    
    Purpose: Class to handle all the requests related to reservation.  

    Args:
        reservation: An object of the type reesrvation which contains details of the current reservation. 

    Functions: 
        Main functions performed include make_reservation, change_availability, cancel_reservation and edit_reservation
    """
    def __init__(self, reservation):
        self.reservation = Reservation(uuid.uuid4(), *reservation)

    def make_reservation(self):
        """
            Programmer: Vaishnavi Sen and Kaung Khant
            
            Purpose: Stores the reservation details in database and updating the availability of the rooms.   

            Returns: Current reservation object. 
        """
        try: 
            self.change_availability('false')
            main_key = ['reservation_id', 'user_name', 'check_in', 'check_out', 'room_type', 'room_number']
            # Adding reservation to the file 
            with open('data/reservations.csv', mode='a', newline='') as file:
                data_adding = csv.DictWriter(file, fieldnames=main_key)
                data_adding.writerow({
                    'reservation_id': self.reservation.unique_id,
                    'user_name': self.reservation.user_name,
                    'check_in': self.reservation.check_in,
                    'check_out': self.reservation.check_out,
                    'room_type': self.reservation.room_type,
                    'room_number': self.reservation.room_number
                })
                
            return 1 #shows success
        except: 
            return 0 # shows failure

    def change_availability(self, value):
        """
            Programmer: Vaishnavi Sen and Kaung Khant
            
            Purpose: Changes the availability in the database to indicate which rooms are available at some time.

            Args: 
                value: 'true' or 'false', passed by the function that is calling it. 
        """
        try: 
            with open('data/AvailableRooms.csv', mode="r") as file:
                read_data = csv.reader(file)
                header = next(read_data)
                rows = []

                for row in read_data:
                    if row[0] == self.reservation.room_number:
                        start_date = datetime.strptime(self.reservation.check_in, '%Y-%m-%d')
                        end_date = datetime.strptime(self.reservation.check_out, '%Y-%m-%d')
                        current_date = start_date
                        while current_date <= end_date:
                            row[header.index(current_date.strftime('%Y-%m-%d'))] = value
                            current_date += timedelta(days=1)
                    rows.append(row)

            # write the updated data back to the csv file
            with open('data/AvailableRooms.csv', mode='w') as file:
                write_data = csv.writer(file)
                write_data.writerow(header)
                write_data.writerows(rows)

            return 1 # shows success 
        # if there is an error with the way the method is working 
        except: 
            return 0 # shows failure        

    # Removing the reservation from csv file after canceling, using pandas
    def cancel_reservation(self, cancel_reservation_id):
        """
            Programmer: Vaishnavi Sen and Kaung Khant
            
            Purpose: Removes the reservation from the database and updates the available rooms.   

            Args: 
                cancel_reservation_id: id of the reservation that is being cancelled.
        """
        try: 
            self.change_availability("true")
            
            # Reading the data from CSV file using pandas
            read_data = pd.read_csv('data/reservations.csv')

            # Remove the canceled reservation from the DataFrame
            read_data.drop(cancel_reservation_id.index, inplace=True)
            
            # Updating data to CSV file after removing reservation that got canceled
            read_data.to_csv('data/reservations.csv', index=False)
            return 1 #shows success
        except: 
            return 0 #shows failure

    # Editing the reservation according to user preference and User ID is unique key
    def edit_reservation(self, **changes):
        """
            Programmer: Vaishnavi Sen
            
            Purpose: Edit the reservation with new values.  

            Args: 
                **changes: the value that is to be change and it's new value should be passed. It is 
                            possible to give multiple changes. 
 
        """
        try: 
            self.cancel_reservation(find_reservation(self.reservation.user_name, self.reservation.check_in, self.reservation.check_out))
            for key, val in changes.items(): 
                if key == 'new_check_in':
                    self.reservation.check_in = val
                if key == 'new_check_out':
                    self.reservation.check_out = val
                if key == 'new_room_type':
                    self.reservation.room_type = val
                    self.reservation.room_number = find_room_number(self.reservation.check_in, self.reservation.check_out, self.reservation.room_type)
        
            self.make_reservation()
            return 1 #shows success
        except: 
            return 0 #shows failure