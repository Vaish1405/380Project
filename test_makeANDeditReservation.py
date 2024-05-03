from Reservation.ReservationController import Reservation, ReservationController

def test_makeANDeditReservation():
    reservation = ['kaung k', '2024-05-03', '2024-05-04', 'standard', '102']
    reservation_controller = ReservationController(reservation=reservation)
    assert reservation_controller.make_reservation() == 1
    assert reservation_controller.edit_reservation(user_name = 'Kaung Khant', check_out = '2024-05-06') == 1