import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/hats"

st.title("🎩 Hat Inventory Management System")

st.header("Add a new hat")
name = st.text_input("Hat Name")
color = st.text_input("Hat Color")

if st.button("Add Hat"):
    if not name or not color:
        st.error("Please fill in all fields")
    else:
        response = requests.post(API_URL, json={"name": name, "color": color})
        if response.status_code == 200:
            st.success("Hat added successfully")
        else:
            st.error(f"Failed to add hat: {response.text}")

st.header("Hat Inventory")
if st.button("Load Hats"):
    response = requests.get(API_URL)
    
    hats = response.json()

    for hat in hats:
        st.write(f"🆔 ID: {hat['id']} | 🎩 {hat['name']} | 🎨 {hat['color']} | 📏 {hat['size']}")

st.header("Update a Hat")
hat_id = st.number_input("Hat ID", min_value=1, step=1)
new_name = st.text_input("New Hat Name")
new_color = st.text_input("New Hat Color")
new_size = st.selectbox("New Hat Size", ["Small", "Medium", "Large", "Extra Large"])

if st.button("Update Hat"):
    response = requests.put(f"{API_URL}/{hat_id}/", json={"name": new_name, "color": new_color, "size": new_size})
    if response.status_code == 200:
        st.success("Hat updated successfully")
    else:
        st.error("Failed to update hat")

st.header("Sell a Hat")
sell_hat_id = st.number_input("Hat ID to Sell", min_value=1, step=1)

if st.button("Mark as Sold"):
    response = requests.delete(f"{API_URL}/{sell_hat_id}/")
    if response.status_code == 200:
        st.success("Hat marked as sold")
    else:
        st.error("Failed to mark hat as sold")
