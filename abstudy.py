# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 18:03:28 2022

@author: Willni
"""
def getGovPayment(income):
    payment = DEFAULT_PAYMENT
    if (income > 452 and income < 542):
        payment = payment - (0.5*(income-452))
    else:
        payment = payment - 45 - (0.6*(income-542))
    if (payment < 0):
        return 0
    else:
        return payment

income_fortnight = 700
DEFAULT_PAYMENT = 660
abstudy = getGovPayment(income_fortnight)
print("Users income is: $", income_fortnight)
print("Payment recieved: $", abstudy)
print("\nTotal: $", (income_fortnight + abstudy))


