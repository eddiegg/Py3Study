from RealtorSys.Rental import Rental
from RealtorSys.House import House
from RealtorSys.Apartment import Apartment
from RealtorSys.Purchase import Purchase


class HouseRental(Rental, House):
    @staticmethod
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init

class ApartmentRental(Rental, Apartment):
    @staticmethod
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init

class ApartmentPurchase(Purchase, Apartment):
    @staticmethod
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init

class HousePurchase(Purchase, House):
    @staticmethod
    def prompt_init():
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init
