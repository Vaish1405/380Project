import csv
from reservation import change_availability

# Removing the reservation from csv file after canceling
def cancel_reservation(user_name):
    # Defining the fields of csv file
    main_key = ['user_name', 'check_in', 'check_out', 'room_type']

    # This list restores the remaining reservation data from CSV file after canceling
    restore_data = []

    # Reading the data in CSV file
    with open('reservations.csv', 'r') as file:
        # Create a CSV reader object
        csv_reader = csv.DictReader(file)

        for r in csv_reader:
            # Checking if the username in CSV file data is the same as the username for canceling reservation
            if r['user_name'] != user_name: # Could also be used with user_id here
                restore_data.append(r)

    # Editing the data in CSV again by removing the canceled reservation
    with open('reservations.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=main_key)
        # Editing the data in csv file without the reservation that has been canceled
        writer.writerows(restore_data)

    # Giving message to inform the user the reservation cancellation is made
    return "Reservation canceled successfully."


def edit_reservation(self, user_id, **kwargs):
    """
     user_id must be included for each reservation changes for each customer in the database
     Using **kwargs which is flexible for variable number of keyword arguments which are the changes to be made
     Examples would be all possible options check_in, check_out and room_type
   """

    # Defining the data we could change according to the user's preference
    change_data = ['room_type', 'check_in', 'check_out']

    for key, value in kwargs.items():
        # Checking if the provided key is one of the editable fields
        if key in change_data:
            # Update the corresponding attribute of the reservation
            setattr(self.reservation, key, value)

    # Read the existing reservations from the CSV file
    with open('reservations.csv', 'r') as file:
        data_reader = csv.DictReader(file)
        read_rows = list(data_reader)

    # Write the modified reservation data back to the file
    with open('reservations.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=['user_name', 'check_in', 'check_out', 'room_type'])
        writer.writeheader()
        for row in read_rows:
            # Tracking reservation information by the User ID
            if row['user_name'] == user_id:
                # Editing the reservation details for any specific customer
                row['room_type'] = self.reservation.room_type
                row['check_in'] = self.reservation.check_in
                row['check_out'] = self.reservation.check_out
            # Changing the data the CSV file according to reservation changes
            writer.writerow(row)

    # Updating room availability based on the reservation changed by customer, essential for specific changes in rooms availability only
    for stored_data, value in kwargs.items():
        if stored_data == 'room type':
            change_availability(self.reservation.room_type)
    return "Your reservation has been updated successfully!"