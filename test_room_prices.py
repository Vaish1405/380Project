from Rooms import get_room_price

def test_get_room_price(): 
    assert get_room_price("standard") == 109
    assert get_room_price("deluxe") == 309
    assert get_room_price("superdeluxe") == 509
    assert get_room_price("invalid") == 0