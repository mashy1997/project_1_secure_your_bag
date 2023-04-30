class CustomerTransaction:

    def __init__(self, description, amount, merchant, category, id = None):
        self.description = description
        self.amount = amount
        self.merchant = merchant
        self.category = category
        self.id = id