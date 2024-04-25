import datetime
def check_validity(check_in_date, check_out_date, num_people):
    """
    Programmer: Kaung Khant

    Date:
    
    Purpose: Function for input validation during date selection. It checks to ensure that the dates selected are logical and 
            number of people for the reservation are not more than maximum.  

    Args:
        check_in_date: Start date of the reservation.
        check_out_date: End date of the reservation. 
        num_people: Number of people in the reservation. 

    Returns:
        string: A custom message indicating success or errors.  
    """
    try:
        # Convert string inputs to datetime.date and int
        check_in_date = datetime.datetime.strptime(check_in_date, '%Y-%m-%d').date()
        check_out_date = datetime.datetime.strptime(check_out_date, '%Y-%m-%d').date()
        num_people = int(num_people)
    except ValueError:
        return "Invalid date or number format."
    
    # Check if dates are in the past
    if check_in_date < datetime.date.today() or check_out_date < datetime.date.today():
        return "Check-in and Checkout dates cannot be past dates."

    # Check if check-in date is after check-out date
    if check_in_date >= check_out_date:
        return "Check-in date must come before the check-out date."

    # Check if dates are more than 3 months in advance
    if (check_in_date - datetime.date.today()).days > 90 or (check_out_date - datetime.date.today()).days > 90:
        return "Sorry! Reservation dates cannot be more than 3 months in advance."
        # Over the maximum number of people per reservation limit
    if num_people > 6:
        return "Maximum number is limited to 6."
    if num_people < 1: 
        return "At least one person per reservation."

    return "Welcome to LA Hotels! The rooms available for reservation are as follows!"
