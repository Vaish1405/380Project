from utility.ValidateAvailabilityInput import check_validity

def test_ValidateAvailabilityInput():
    assert check_validity("2024-04-28", "2024-05-04","5") == "Check-in and Checkout dates cannot be past dates."
    assert check_validity("2024-05-07", "2024-05-03","3") == "Check-in date must come before the check-out date."
    assert check_validity("2024-09-10", "2024-09-12", "5") == "Sorry! Reservation dates cannot be more than 3 months in advance."
    assert check_validity("2024-05-05", "2024-05-08", "8") == "Maximum number is limited to 6."
    assert check_validity("2024-05-10", "2024-05-12", "0") == "At least one person per reservation."
    assert check_validity("2024-05-03", "2024-05-05", "3") == "Welcome to LA Hotels! The rooms available for reservation are as follows!"
    assert check_validity("10-05-2024", "12-05-2024", "4") == "Invalid date or number format."
