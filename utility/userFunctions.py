import csv

class User:
    def __init__(self, user_name, email, phone, password):
        self.user_name = user_name
        self.email = email
        self.phone = phone
        self.password = password

def upload_user(user_name, user_email, user_phone, user_password):
     with open('data/users.csv', 'a', newline='') as csvfile:
        fieldnames = ['user_name', 'user_email', 'user_phone', 'user_password']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if csvfile.tell() == 0:
            writer.writeheader()

        writer.writerow({
            'user_name': user_name,
            'user_email': user_email, 
            'user_phone': user_phone, 
            'user_password': user_password})


def find_user(email):
    with open('data/users.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['user_email'] == email:
                return User(row['user_name'], row['user_email'], row['user_phone'], row['user_password'])
        return None