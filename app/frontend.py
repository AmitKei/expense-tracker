import streamlit as st
import requests

BASE_URL = "http://localhost:8000"

st.title("💸 Expense Tracker")

username = st.text_input("Enter your username:")
if not username:
    st.warning("Please enter a username to continue.")
    st.stop()

headers = {"username": username}

st.subheader("➕ Add Expense")
desc = st.text_input("Description")
amount = st.number_input("Amount", min_value=0.0)
category = st.selectbox("Category", ["Food", "Transport", "Leisure", "Utilities", "Other"])
if st.button("Add"):
    if desc and amount:
        data = {"description": desc, "amount": amount, "category": category}
        res = requests.post(f"{BASE_URL}/expenses", json=data, headers=headers)
        st.success("Added!" if res.ok else res.text)

st.subheader("🔍 Search")
search_term = st.text_input("Search by description")
if search_term:
    response = requests.get(f"{BASE_URL}/expenses?search={search_term}", headers=headers)
else:
    response = requests.get(f"{BASE_URL}/expenses", headers=headers)

if response.ok:
    expenses = response.json()
    for exp in expenses:
        st.write(f"**{exp['description']}** - ₪{exp['amount']} ({exp['category']})")
        if st.button(f"Delete #{exp['id']}", key=exp['id']):
            requests.delete(f"{BASE_URL}/expenses/{exp['id']}", headers=headers)
            st.experimental_rerun()

total = requests.get(f"{BASE_URL}/total", headers=headers).json().get("total", 0)
st.sidebar.write(f"**Total:** ₪{total}")
