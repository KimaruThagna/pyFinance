import streamlit as st
from financial_apis import *

st.sidebar.markdown("Welcome to InvestorLytica.")
page = st.sidebar.selectbox("Choose task", ["DCF", "NPV Cashflow", "IRR", "Data Pull"])# pages
intro_text = '''
The discounted Cashflow models is a method of discounting future cashflows of a business at a considerable rate 
to bring it to today's value. \n 
With this formula, one can determine a reasonable intrinsic value of the business they wish to buy.\n
Owners earnings=Cashflow for owners=Operating cashflow-maintenance capEx. If you assume maintenance capEx=total capEx, 
then Owners earnings=FreeCashFlow(FCF)
Operating Cashflow- cash generated from operating activities. Can be found in the cash statement \n
Capital Expenditure (CapEx)- Amount spent on capital assets that will generate revenue for the business long term. Some is used in growth, some in maintenance.\n
Maintenance CapEx percentage- The percentage of capEx that a business used in maintenance of plant property and equipment. \n
0-5 Year growth Rate- Projected percentage growth that this business will have over the next 5 years on its cashflows\n
6-10 Year growth Rate- Projected percentage growth that this business will have over the next 6-10 years on its cashflows. Should ideally be lower that the 0-5.\n
Risk Free Rate (%)- The discount rate that you use to bring future cashflows to present value and hence determine intrinsic value of business. 
This rate is usually the interest on treasury risk free bonds since theyre considered almost risk free. It is believed that its almost impossible for a government to default. \n
Required Return Rate (%)- Your desired rate of return from this business. Will be used to calculate the buying price by discounting future cashflows to present day value. \n
Shares outstanding- The number of pieces of a business that are available in the market. Allows calculation of the buy price per share. If you are buying the whole business, then the share outstanding value becomes 1. \n
Terminal Growth Rate (%) - The rate at which you expect the terminal value of a business to grow. Ideally, for a conservative measure, it should be 0. \n
Terminal value computation is done via the growth perpetuity model with g=0% by default. 
'''
if page == "DCF":

    st.title("Investment Analysis using DCF Model")
    st.header("DCF")
    st.write(intro_text)
    # data input
    st.subheader('Input the required data for Intrinsic value analysis')
    operating_cashflow = st.number_input('Enter the operating Cashflow')
    capex = st.number_input('Enter the business capital expenditure')
    maintenance_capex_percentage = st.number_input('What percentage of capEx is maintenance(%)')
    growth_5 = st.number_input('Expected growth rate as a percentage for the first 5 years of the business(%)')
    growth_10 = st.number_input('Expected growth rate as a percentage for year 6 to year 10 of the business(%)')
    risk_free_discount = st.number_input('Risk Free Discount Rate')
    required_return_rate = st.number_input('Required Return Rate')
    shares_outstanding = st.number_input('Shares outstanding in the business')
    terminal_value_growth_rate = st.number_input('Terminal Value Growth Rate(%)')
    #data computation and output
    if required_return_rate != 0.00 and maintenance_capex_percentage !=  0.00 \
        and risk_free_discount != 0.00:
        cashflows, metrics = dcf(operating_cashflow,(maintenance_capex_percentage/100),capex,
                                 (growth_5/100), (growth_10/100), (risk_free_discount/100), (required_return_rate/100),
                                 shares_outstanding, (terminal_value_growth_rate/100) )
        st.subheader('Business Projected Cashflows over 10 Yrs')
        st.dataframe(cashflows)
        st.subheader('Business Projected Metrics')
        st.dataframe(metrics)


elif page == "NPV Cashflow":

    st.title("NPV Cashflow")
    st.header("Analyze Cashflows in NPV")
    st.text("Use this simple calculator to determine if an investment will be net positive considering cashflows and returns discounted"
            "to present value.")
    initial_investment = st.number_input('Initial Investment')
    annual_return = st.number_input('What you project to be getting annually in returns')
    annual_growth_rate = st.number_input('Projected annual growth rate of returns')
    years = st.number_input('Number of years you plan to hold onto the investment')
    terminal_value = st.number_input('What you project to sell your stake for')


elif page == "IRR":

    st.title("IRR")
    st.header("Evaluate Businesses using the IRR and MIRR methods")
    st.text(
        "Use this simple calculator to determine your required rate of return and baselines.")

elif page == "Data Pull":

    st.title("Financial Data")
    st.header("Financial Data from Financial model Prep API Resource")
    st.text("Main URL: https://financialmodelingprep.com/api/v3/")
    ticker = st.text_input("Enter Ticker symbol")
    ticker = ticker.upper()
    if ticker:
        profile_defaults = ['symbol', 'price']
        st.subheader('Company Profile')
        data = company_profile(ticker)
        selected_columns = st.multiselect('Select desired Columns', data.columns.to_list(), default=profile_defaults)
        st.dataframe(data[selected_columns])

        #metrics
        metrics_defaults = ['symbol', 'date', 'revenuePerShare']
        ratios_defaults = ['symbol', 'date', 'currentRatio']
        st.subheader('Company Financial Metrics')
        metrics = company_financial_metrics(ticker)
        metrics_selected_columns = st.multiselect('Select desired Columns', metrics.columns.to_list(), default=metrics_defaults)
        st.dataframe(metrics[metrics_selected_columns])
        # ratios
        st.subheader('Company Financial Ratios')
        ratios = company_financial_ratios(ticker)
        ratios_selected_columns = st.multiselect('Select desired Columns', ratios.columns.to_list(), default=ratios_defaults)
        st.dataframe(ratios[ratios_selected_columns])

        # growth
        growth_defaults = ['symbol', 'date', 'revenueGrowth']
        st.subheader('Company Projected growth')
        growth = company_growth_figures(ticker)
        growth_selected_columns = st.multiselect('Select desired Columns', growth.columns.to_list(), default=growth_defaults)
        st.dataframe(growth[growth_selected_columns])

        # dcf
        dcf_defaults = ['symbol', 'date', 'dcf']
        st.subheader('Company Estimated DCF From API')
        dcf = company_dcf_api(ticker)
        dcf_selected_columns = st.multiselect('Select desired Columns', dcf.columns.to_list(),
                                                 default=dcf_defaults)
        st.dataframe(dcf[dcf_selected_columns])

        # balance sheet
        balance_defaults = ['date', 'Cash and cash equivalents']
        st.subheader('Company Balance sheet')
        balance_sheet = company_balance_sheet(ticker)
        selected_columns = st.multiselect('Select desired Columns', balance_sheet.columns.to_list(),
                                                 default=balance_defaults)
        st.dataframe(balance_sheet[selected_columns])

        #cashflow statement
        balance_defaults = ['date', 'Cash and cash equivalents']
        st.subheader('Company Balance sheet')
        balance_sheet = company_balance_sheet(ticker)
        selected_columns = st.multiselect('Select desired Columns', balance_sheet.columns.to_list(),
                                          default=balance_defaults)
        st.dataframe(balance_sheet[selected_columns])

        # income


#THINK OF GRAPHS
