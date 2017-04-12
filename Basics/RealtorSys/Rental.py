from RealtorSys.Validator import get_valid_input


class Rental:
    def __init__(self, furnished='', utilities='', rent='', **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        super().display()
        print('''
        RENTAL DETAILS
        rent: {}
        estimated utilities: {}
        furnished: {}
        '''.format(self.rent, self.utilities, self.furnished))

    @staticmethod
    def prompt_init():
        return dict(
            rent=input("What is the monthly rent? "),
            utilities=input("What are the estimated utilities? "),
            furnished=get_valid_input("Is the property furnished? ", ("yes", "no"))
        )
