from Extras import get_extras_price

def test_get_extras_price():
    assert get_extras_price("shuttle") == 100
    assert get_extras_price("pet") == 200
    assert get_extras_price("invalid") == 0