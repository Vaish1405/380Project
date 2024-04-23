import pandas as pd

def find_reservation(user_name, check_in, check_out):
    read_data = pd.read_csv('data/reservations.csv')
    reservation_data = read_data[(read_data['user_name'] == user_name) & 
                                 (read_data['check_in'] == check_in) & 
                                 (read_data['check_out'] == check_out)]

    return reservation_data