class Apartment(Property):
    valid_laundries = ("coin","ensuite","none")
    valid_balconies = ("yes","no","solarium")

    def __init__(self, balcony='',laundry='', **kwargs):
