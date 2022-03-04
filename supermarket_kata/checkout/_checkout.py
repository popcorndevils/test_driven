class Checkout:
    class Discount:
        def __init__(self, nbr_items, price):
            self.nbr_items = nbr_items
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.cart = {}

    def add_item_price(self, item, value):
        self.prices[item] = value

    def add_item(self, item, amt = 1):
        if item in self.prices:
            self.cart[item] = self.cart.get(item, 0) + amt
        else:
            raise Exception(f"Item {item} is unknown.")

    def calculate_total(self):
        _total = 0
        for k, v in self.cart.items():
            if k in self.discounts and self.discounts[k].nbr_items <= v:
                _d = self.discounts[k]
                _unit_price = _d.price / _d.nbr_items
                _total += v * _unit_price
            else:
                _total += self.prices[k] * v
        return _total

    def add_discount(self, item, min, price):
        _discount = self.Discount(min, price)
        self.discounts[item] = _discount
