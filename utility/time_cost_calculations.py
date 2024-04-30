from datetime import datetime
from Rooms import get_room_price
from Extras import get_extras_price

def getDays(checkIn, checkOut):
    checkIn = datetime.strptime(checkIn, "%Y-%m-%d")
    checkOut = datetime.strptime(checkOut, "%Y-%m-%d")

    nights = (checkOut - checkIn).days 
    return nights

def get_total(nights, room_selection, extras_selection):
    sum = 0
    sum += int(get_room_price(room_selection)) * int(nights)
    sum += int(get_extras_price(extras_selection))
    sum += 50
    return sum  