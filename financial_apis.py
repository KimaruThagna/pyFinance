import requests, os
import pandas as pd
from dotenv import load_dotenv
from dcf import dcf
load_dotenv()

root_url = 'https://financialmodelingprep.com/api/v3/'


def data_pull(domain, ticker_symbol, params=None):
    key = os.getenv('API_KEY')
    PARAMS = {'apikey': key}
    if params:
        PARAMS.update(params)

    try:
        data = requests.get(url=f'{root_url}{domain}/{ticker_symbol}', params=PARAMS)
        return data.json()
    except Exception as e:
        return [{"Error":f'An error occured{e}'}]

def company_profile(ticker_symbol):

    return pd.DataFrame(data_pull('profile', ticker_symbol))

def company_income_statement(ticker_symbol):

    annual_income_statement = data_pull('financials/income-statement', ticker_symbol, params={'period':'annual'})
    annual_balance_sheet = data_pull('financials/balance-sheet-statement', ticker_symbol, params={'period':'annual'})
    annual_cashflow_statement = data_pull('financials/cash-flow-statement', ticker_symbol, params={'period':'annual'})
    return pd.DataFrame(annual_income_statement['financials'])

def company_balance_sheet(ticker_symbol):
    annual_balance_sheet = data_pull('financials/balance-sheet-statement', ticker_symbol, params={'period':'annual'})
    return pd.DataFrame(annual_balance_sheet['financials'])

def company_cashflow(ticker_symbol):
    annual_cashflow_statement = data_pull('financials/cash-flow-statement', ticker_symbol, params={'period':'annual'})
    return pd.DataFrame(annual_cashflow_statement['financials'])

def company_financial_ratios(ticker_symbol):
    ratios = data_pull('ratios', ticker_symbol)
    return  pd.DataFrame(ratios)


def company_financial_metrics(ticker_symbol):
    metrics = data_pull('key-metrics', ticker_symbol)
    return pd.DataFrame(metrics)

def company_dcf_analysis(ticker_symbol):
    pass

def company_dcf_api(ticker_symbol):

    return pd.DataFrame(data_pull('discounted-cash-flow', ticker_symbol))

def company_growth_figures(ticker_symbol):
    growth = data_pull('financial-growth', ticker_symbol)

    return pd.DataFrame(growth)
