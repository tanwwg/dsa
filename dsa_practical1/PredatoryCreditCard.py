from CreditCard import CreditCard

class PredatoryCreditCard(CreditCard):

    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr
        self._charge_times = 0

    def charge_for_time(self):
        self._charge_times += 1
        if self._charge_times > 10:
            self._balance += 1

    def charge(self, price):
        self.charge_for_time()

        charge_ret = super().charge(price)
        if not charge_ret:
            self._balance += 5
        return charge_ret

    def process_month(self):
        mul = pow(1 + self._apr, 1/12)
        self._balance *= mul

if __name__ == '__main__':
    wallet = []
    wallet.append(PredatoryCreditCard('John Lee',
    'DBS',
    '5391 0375 9387 5309', 2500, 0.1) )
    wallet.append(PredatoryCreditCard('John Lee',
    'OCBC',
    '3485 0399 3395 1954', 3500, 0.1) )
    wallet.append(PredatoryCreditCard('John Lee',
    'Maybank',
    '5391 0375 9387 5309', 5000, 0.1) )

    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)

    for c in range(3):
        print('Customer =', wallet[c].get_customer())
        print('Bank =', wallet[c].get_bank())
        print('Account =', wallet[c].get_account())
        print('Limit =', wallet[c].get_limit())
        print('Balance =', wallet[c].get_balance())
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
        print('New balance =', wallet[c].get_balance())
        print()