class Reservation:
    """
    Programmer: Vaishnavi Sen and Kaung Khant
    
    Purpose: Declaring the Reservation Class. 

    Args:
        unique_id: Unique id that represents the reservation in the database. 
        check_in: Start date of the reservation. 
        check_out: End date of the reservation. 
        room_type: Type of the room selected by the user. 
        room_number: Room number allocated for the reservation. 
        
    """
    def __init__(self, unique_id, user_name, check_in, check_out, room_type, room_number):
        self.unique_id = unique_id
        self.user_name = user_name
        self.check_in = check_in
        self.check_out = check_out
        self.room_type = room_type
        self.room_number = room_number