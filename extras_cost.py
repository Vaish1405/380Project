class shuttle():
    def get_price(self):
        return 100
    
class pet():
    def get_price(self):
        return 200
    
def get_extras_price(selection):
    selection = selection.lower()
    if selection == "shuttle":
        return shuttle().get_price()
    elif selection == "pet":
        return pet().get_price()
    else: 
        return 0