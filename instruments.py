"""
Financial Instruments
"""


class Instrument(object):
    """
    Base Instrument class
    """
    is_liability = False

    def __init__(self, value, rate=0, fee=0):
        self._value = value
        self._rate = rate
        self._fee = fee

    @property
    def value(self):
        return self._value

    @property
    def rate(self):
        return self._rate

    @property
    def fee(self):
        return self._fee

    def interest(self):
        return self._value * self._rate

    def add_value(self, amount):
        self._value += amount

    def subtract_value(self, amount):
        self._value -= amount

    def net_wealth(self):
        if self.is_liability:
            return -self.value
        else:
            return self.value


class BankAccount(Instrument):
    def __init__(self, balance, rate):
        self._principal = balance
        super().__init__(value=-balance, rate=rate)

    @property
    def balance(self):
        return self._value

    def transfer_to(self, other, amount):
        self.subtract_value(amount)
        other.add_value(amount)


class HomeLoan(Instrument):

    is_liability = True

    def __init__(self, principal, rate, term=30 * 12, fee=0):
        self._principal = principal
        self._term = term
        super().__init__(value=principal, rate=rate, fee=fee)

    def monthly_payment(self):
        return self._principal * self._rate * (1 + self._rate) ** self._term / (
                (1 + self._rate) ** self._term - 1)


FixedRateLoan = HomeLoan


class VariableRateLoan(HomeLoan):

    def set_offset_account(self, account):
        self._offset_account = account

    def interest(self):
        try:
            value_for_interest = max(self.value - self._offset_account.value, 0)
        except:
            value_for_interest = self.value
        return value_for_interest * self._rate
