import streamlit as st

st.title("🏦 Banking System")

balance = 1000

option = st.selectbox("Choose option", ["Deposit", "Withdraw", "Check Balance"])

if option == "Deposit":
    amount = st.number_input("Enter amount", min_value=1)
    if st.button("Deposit"):
        balance += amount
        st.success("Deposited successfully")

elif option == "Withdraw":
    amount = st.number_input("Enter amount", min_value=1)
    if st.button("Withdraw"):
        if amount <= balance:
            balance -= amount
            st.success("Withdraw successful")
        else:
            st.error("Insufficient balance")

elif option == "Check Balance":
    st.info(f"Balance: {balance}")