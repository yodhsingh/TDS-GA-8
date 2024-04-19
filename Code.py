import streamlit as st
st.title('Maximum of three numbers')
st.header("Enter three numbers")
st.subheader("in the boxes below")
a, b, c = st.number_input(), st.number_input(), st.number_input()
st.write("**Maximum** _value_ :)
st.write(max(a,b,c))
