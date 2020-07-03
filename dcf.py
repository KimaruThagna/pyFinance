import numpy as np
import pandas as pd
import os

'''
The discounted Cashflow models is a method of discounting future cashflows of a business at a considerable rate 
to bring it to today's value. With this formula, one can determine a reasonable intrinsic value of the business they wish to buy
Owners earnings=Cashflow for owners=Operating cashflow-maintenance capEx. If you assume maintenance capEx=total capEx, 
then Owners earnings=FreeCashFlow(FCF)
'''

def dcf(free_cashflow, maintenance_capex_percentage, capex, growth_rate_5, growth_rate_10,
        risk_free_discount_rate, required_return_rate, shares_outstanding=1,
        terminal_val_growth=0):

    owners_earnings = free_cashflow - (capex*maintenance_capex_percentage)
    discounted_cashflows = []
    # perform cashflow projections for the first 5 years and discount to present value
