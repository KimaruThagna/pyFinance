import requests, os
from dotenv import load_dotenv
load_dotenv()

root_url = 'https://financialmodelingprep.com/api/v3/'


def data_pull(ticker_symbol):
    key = os.getenv('API_KEY')
    url = f'{root_url}'
    pass

def company_profile(ticker_symbol):
    pass

def company_financial_statements(ticker_symbol):
    pass

def company_financial_ratios_and_metrics(ticker_symbol):
    pass

def company_dcf_analysis(ticker_symbol):
    pass

def company_dcf_api(ticker_symbol):
    pass

def company_growth_figures(ticker_symbol):
    pass