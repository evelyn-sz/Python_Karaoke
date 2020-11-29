class Bar:
    
    def __init__(self, name, till):
        self.name = name
        self.till = till

    def verify_age(self, guest):
        if guest.age >= 18:
            return True
        else:
            return False

    def refuse_drink_sale(self):
        pass