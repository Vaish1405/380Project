class Reservation:
    def __init__(self, unique_id, user_name, check_in, check_out, room_type, room_number):
        self.unique_id = unique_id
        self.user_name = user_name
        self.check_in = check_in
        self.check_out = check_out
        self.room_type = room_type
        self.room_number = room_number