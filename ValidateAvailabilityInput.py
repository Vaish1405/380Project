import datetime
def check_availability(check_in_date, check_out_date, num_people):
    # Check if dates are in the past
    if check_in_date < datetime.date.today() or check_out_date < datetime.date.today():
        return "Sorry! Check-in and Checkout dates cannot be past dates.\nPlease try again."

    # Check if check-in date is after check-out date
    if check_in_date >= check_out_date:
        return "Sorry! Check-in date must come before the check-out date.\nPlease try again."

    # Check if dates are more than 3 months in advance
    if (check_in_date - datetime.date.today()).days > 90 or (check_out_date - datetime.date.today()).days > 90:
        return "Sorry! Reservation dates cannot be more than 3 months in advance.\nPlease try again."
        # Over the maximum number of people per reservation limit
    if num_people > 6 or num_people <= 0:
        return ("Sorry! At least one person per reservation and maximum number is limited to 6.\nPlease try again.")

    return f"Welcome to LA Hotels! The rooms available for reservation are as follows!"


# Check-in, Check-out, and Num of People
def make_reservation(check_in_date, check_out_date, num_people):
    availability_result = check_availability(check_in_date, check_out_date, num_people)
    if availability_result:
        return availability_result

    # Check-out Date should be at least 1 or more than Check-in Date
    reservation_validity = len(reservation_dates) + 1
    reservation_dates[reservation_validity] = (check_in_date, check_out_date)
    return f"Welcome to LA Hotels! The rooms available for reservation are as follows!"


# Dictionary to store reservations
reservation_dates = {}

# Default values for Check-in and Checkout
check_in = datetime.date(2024, 3, 5)
check_out = datetime.date(2024, 3, 10)

print(make_reservation(check_in, check_out, 0))  # Reservation by default for now
