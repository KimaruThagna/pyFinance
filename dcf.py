import numpy as np
import pandas as pd
import os

'''
The discounted Cashflow models is a method of discounting future cashflows of a business at a considerable rate 
to bring it to today's value. With this formula, one can determine a reasonable intrinsic value of the business they wish to buy
Owners earnings=Cashflow for owners=Operating cashflow-maintenance capEx. If you assume maintenance capEx=total capEx, 
then Owners earnings=FreeCashFlow(FCF)
'''

def dcf(operating_cashflow, maintenance_capex_percentage, capex, growth_rate_5, growth_rate_10,
        risk_free_discount_rate, required_return_rate, shares_outstanding=1,
        terminal_val_growth=0):

    owners_earnings = operating_cashflow - (capex*maintenance_capex_percentage)
    projected_cashflows = []
    year_5_val = 0
    year_10_val = 0
    current_cashflow = owners_earnings
    # perform cashflow projections for the first 5 years
    for year in range(6):
        data_line = [f'year{year}', current_cashflow]
        current_cashflow += growth_rate_5*current_cashflow # same as current_cashflow = 1+growth_rate_5*current_cashflow
        projected_cashflows.append(data_line)
        if year == 5:
            year_5_val = current_cashflow
    # perform cashflow projections for the next 5 years
    current_cashflow = year_5_val
    for year in range(6,11):
        data_line = [f'year{year}', current_cashflow]
        current_cashflow += growth_rate_10 * current_cashflow  # same as current_cashflow = 1+growth_rate_5*current_cashflow
        projected_cashflows.append(data_line)
        if year == 9: # calculate terminal value
            # Formula TV  =  (Owners earnings_Yr10 x (1 + g))  /  (discount_rate – g) where g=terminal_growth_rate
            year_10_val = current_cashflow

    intrinsic_terminal_value = (year_10_val+(1+terminal_val_growth)) / (risk_free_discount_rate-terminal_val_growth)
    buy_terminal_value = (year_10_val + (1 + terminal_val_growth)) / (required_return_rate - terminal_val_growth)
    data_line1 = ["Intrinsic Terminal Value", np.round(intrinsic_terminal_value, 2)]
    data_line2 = ["Buy Price Terminal Value", np.round(buy_terminal_value, 2)]
    projected_cashflows.append(data_line1)
    projected_cashflows.append(data_line2)

    #create projected cashflows dataframe
    column_names = ['Year', 'ProjectedCashflow']

    projected_cashflows_df = pd.DataFrame(projected_cashflows, columns=column_names)
    # exclude year 0
    cashflow_list = projected_cashflows_df['ProjectedCashflow'].tolist()[1:]
    intrinsic_value_list = cashflow_list[:-1]

    business_intrinsic_value = np.npv(risk_free_discount_rate, intrinsic_value_list)

    buy_price_list = cashflow_list[:-2]
    buy_price_list.append(buy_terminal_value)

    business_buy_price = np.npv(required_return_rate, buy_price_list)
    buy_price_per_share = business_buy_price / shares_outstanding
    # create evaluation DF
    evaluation_data = []
    evaluation_data.append(['Business Intrinsic Value', np.round(business_intrinsic_value, 2)])
    evaluation_data.append(['Business Buy Price', np.round(business_buy_price,2)])
    evaluation_data.append(['Buy Price per Share', np.round(buy_price_per_share, 2)])
    evaluation_data.append(['Shares Outstanding', np.round(shares_outstanding,2)])
    headers = ['Metric', 'Value']
    evaluation_df = pd.DataFrame(evaluation_data, columns=headers)

    return projected_cashflows_df, evaluation_df

#print(dcf(175, 0.6, 100, 0, 0, 0.03, 0.22))