from utility import getDays
from utility import get_total

def test_getDays():
    #seeing if it calculates days correctly (checkOut - checkIn)
    checkIn = "2024-05-01"
    checkOut = "2024-05-05"
    assert getDays(checkIn,checkOut) == 4 

    #what if its on same day -- should return 0
    checkIn = "2024-05-01"
    checkOut = "2024-05-01"
    assert getDays(checkIn,checkOut) == 0

    #booking for more than a month (30 or 31 days depending on month)
    checkIn = "2024-05-05"
    checkOut = "2024-07-04"
    assert getDays(checkIn,checkOut) == 60
    #assert getDays(checkIn, checkOut) < 30 or getDays(checkIn,checkOut) < 31, "No more than a month."

def test_get_total():
    nights = 4
    room_selection = "deluxe" #309
    #309*4 = 1236 for 4 days in deluxe
    extras_selection = "pet" #200
    #1236 + 200 = 1436
    #+50 for tax = 1486
    assert get_total(nights,room_selection,extras_selection) == 4 * 309 + 200 + 50

    nights = 2
    room_selection = "superdeluxe" #509
    extras_selection = "shuttle" #100
    assert get_total(nights,room_selection,extras_selection) == 2 * 509 + 100 + 50

    #wrong room_selection type
    nights = 3
    room_selection = "heaven feel" #509
    extras_selection = "shuttle" #100
    assert get_total(nights,room_selection,extras_selection) == 3 * 0 + 100 +50
    #room_selection != "standard" or "deluxe" or "superdeluxe",0


