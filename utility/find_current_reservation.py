import pandas as pd
from Reservation import find_reservation

def find_current_reservation(user_name):
    users_df = pd.read_csv('data/users.csv')
    reservations_df = pd.read_csv('data/reservations.csv')

    merged_df = pd.merge(users_df, reservations_df, on="user_name")

    for index, row in merged_df.iterrows():
        if row['user_name'] == user_name:
            return find_reservation(row['user_name'], row['check_in'], row["check_out"])
    
    return 0
    

# print(find_current_reservation('Vaish Sen')['user_name'])