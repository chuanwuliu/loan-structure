"""
Projection Engine.

Given the total loan amount which includes a variable part and a fixed rate

Calculate the amount of variable rate loan based on monthly saving
"""

from instruments import *
from config import *


def project_wealth(p_var, p_fixed, period=3 * 12):
    bank_account = BankAccount(balance=0, rate=0)
    saving_account = BankAccount(balance=0, rate=r_saving)
    fixed_rate_loan = FixedRateLoan(principal=p_fixed, rate=r_fix, term=term)
    variable_rate_loan = VariableRateLoan(principal=p_var, rate=r_var, term=term,
                                          fee=var_loan_monthly_fee)
    variable_rate_loan.set_offset_account(bank_account)
    for i in range(period):
        bank_account.add_value(salary - living_cost)
        for loan in [fixed_rate_loan, variable_rate_loan]:
            bank_account.subtract_value(loan.monthly_payment())
            bank_account.subtract_value(loan.fee)
            loan.subtract_value(loan.monthly_payment() - loan.interest())
        if bank_account.balance > variable_rate_loan.value:
            bank_account.transfer_to(saving_account, bank_account.value - variable_rate_loan.value)
        # print(saving_account.balance, bank_account.balance, fixed_rate_loan.value, variable_rate_loan.value)
    return saving_account.net_wealth() + bank_account.net_wealth() + fixed_rate_loan.net_wealth() + variable_rate_loan.net_wealth()


#print(project_wealth(50000, 440000))
