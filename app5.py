import streamlit as st

#off_promotion = st.number_input("Promotion (A to SA)",0.0,10.0, step = 1.0, key="oflev1")
#st.write(off_promotion)

#number1 = st.number_input('Insert a number')
#number2 = number1
#number3 = number2*4
#st.write('This is the final value. ',number3)

number1 = st.number_input('Insert a number',step=3.0, key=2)
number2 = st.number_input('Insert a number',step=3.0, key=1)
st.write(f"This is {number1}+{number2}", number1+number2)
st.write(f"This is {number1}-{number2}",number1-number2)
st.write(f"This is {number1}*{number2}",number1*number2)
