def tax(balance, apr):
    # write the actual function here
    # hint: x ** n will find x to the power of n
    # hint 2: 12th root of x is x ** (1/12)
    return (1+apr)**(1/12)*balance

print(tax(100, 0.0825))
# expect 100.6628




from credit_card import CreditCard

class PredatoryCreditCard(CreditCard):

    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr
        # add more things

    def charge(self, price):
        super_ret = super().charge(price)
        if not super_ret:
            self._balance += 5
        return super_ret
        # do things here

    def process_month(self):
        self._balance = tax(self._balance, self._apr)



card = PredatoryCreditCard('John Lee','DBS', '5391 0375 9387 5309',
                           2500, 0.1)

print(card._balance)
card.charge(2501)
print(card._balance == 5)

