import streamlit as st
from dcf import dcf

st.sidebar.markdown("Welcome to Picture-lytics.")
page = st.sidebar.selectbox("Choose task", ["DCF", "NPV Cashflow", "IRR"])# pages
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
    cashflows, metrics = dcf(operating_cashflow,maintenance_capex_percentage,capex,
                             growth_5, growth_10, risk_free_discount, required_return_rate,
                             shares_outstanding, terminal_value_growth_rate)
    st.subheader('Business Projected Metrics')
    st.dataframe(cashflows)
    st.dataframe(metrics)


elif page == "NPV Cashflow":

    st.title("NPV Cashflow")
    st.header("Analyze Cashflows in NPV")
    st.text("Use this simple calculator to determine if an investment will be net positive considering cashflows and returns discounted"
            "to present value.")

elif page == "IRR":

    st.title("IRR")
    st.header("Evaluate Businesses using the IRR and MIRR methods")
    st.text(
        "Use this simple calculator to determine your required rate of return and baselines.")

