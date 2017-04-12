from RealtorSys.Property import Property
from RealtorSys.Validator import get_valid_input


class Apartment(Property):
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super().display()
        print('''
        APARTMENT DETAILS
        laundry: {0}
        has balcony: {1}
        '''.format(self.laundry, self.balcony))

    @staticmethod
    def prompt_init():
        parent_init = Property.prompt_init()

        # laundry = ''
        # while laundry.lower() not in Apartment.valid_laundries:
        #     laundry = input("What laundry facilities does the property have?"
        #                     " ({}) ".format(", ".join(Apartment.valid_laundries)))
        # balcony = ''
        # while balcony.lower() not in Apartment.valid_balconies:
        #     balcony = input("Does the property hava a balcony?"
        #                     " ({}) ".format(", ".join(Apartment.valid_balconies)))

        laundry = get_valid_input('''
        What laundry facilities does 
        the property have?
        ''', Apartment.valid_laundries)

        balcony = get_valid_input('''
        Does the property have a balcony?
        ''', Apartment.valid_balconies)

        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init


# def get_valid_input(input_string, valid_options):
#     input_string += " ({}) ".format(", ".join(valid_options))
#     response = input(input_string)
#     while response.lower() not in valid_options:
#         response = input(input_string)
#     return response
