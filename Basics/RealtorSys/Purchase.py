class Purchase:
    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        super().display()
        print('''
        PURCHASE DETAILS
        selling price: {}
        estimated taxes: {}
        '''.format(self.price, self.taxes))

    @staticmethod
    def prompt_init():
        return dict(
            price = input("What is the selling price? "),
            taxes = input("What are the estimated taxes? ")
        )