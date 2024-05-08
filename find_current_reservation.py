import pandas as pd
from Reservation import find_reservation

def find_current_reservation(user_name):
    users_df = pd.read_csv('data/users.csv')
    reservations_df = pd.read_csv('data/reservations.csv')

    merged_df = pd.merge(users_df, reservations_df, on='user_name')

    return find_reservation(merged_df['user_name'].values[0], merged_df['check_in'].values[0], merged_df['check_out'].values[0])

print(find_current_reservation('V S'))