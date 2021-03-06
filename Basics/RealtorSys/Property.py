class Property:
    def __init__(self, square_feet='', beds='', baths='', **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        print('''
        PROPERTY DETAILS
        ++++++++++++++++
        squre footage: {0}
        bedrooms: {1}
        bathrooms: {2}
        
        '''.format(self.square_feet, self.num_bedrooms,
                   self.num_baths))

    @staticmethod
    def prompt_init():
        return dict(square_feet = input("Enter the square feet: "),
                    beds = input("Enter number of bedrooms: "),
                    baths = input("Enter number of baths: "))

        # prompt_init = staticmethod(prompt_init)

if __name__ == '__main__':
    print(Property.prompt_init())