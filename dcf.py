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
    projected_cashflows = []
    year_10_val = 0
    # perform cashflow projections for the first 5 years
    for year in range(1,6):
        current_cashflow = owners_earnings
        data_line = [f'year{year}', current_cashflow]
        current_cashflow += growth_rate_5*current_cashflow # same as current_cashflow = 1+growth_rate_5*current_cashflow
        projected_cashflows.append(data_line)
    # perform cashflow projections for the next 5 years
    for year in range(6,11):
        current_cashflow = owners_earnings
        data_line = [f'year{year}', current_cashflow]
        current_cashflow += growth_rate_5 * current_cashflow  # same as current_cashflow = 1+growth_rate_5*current_cashflow
        projected_cashflows.append(data_line)
        if year == 10: # calculate terminal value
            # Formula TV  =  (Owners earnings_Yr10 x (1 + g))  /  (discount_rate – g) g=terminal_growth_rate
            intrinsic_terminal_value = (year_10_val+(1+terminal_val_growth)) / (risk_free_discount_rate-terminal_val_growth)
            buy_terminal_value = (year_10_val + (1 + terminal_val_growth)) / (required_return_rate - terminal_val_growth)
            data_line1 = ["Intrinsic Terminal Value", intrinsic_terminal_value]
            data_line2 = ["Buy Price Terminal Value", buy_terminal_value]
            projected_cashflows.append(data_line1)
            projected_cashflows.append(data_line2)

