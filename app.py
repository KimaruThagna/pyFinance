import streamlit as st


st.sidebar.markdown("Welcome to Picture-lytics.")
page = st.sidebar.selectbox("Choose task", ["DCF", "NPV Cashflow"])# pages
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
    # file upload and handling logic


elif page == "NPV Cashflow":

    st.title("Image Classification with Google's Teachable Machine")
    st.header("Brain Tumor MRI Classification Example")
    st.text("Upload a brain MRI Image for image classification as tumor or no-tumor")
