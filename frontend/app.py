
import streamlit as st
import requests

# Define the base URL for your FastAPI backend
BASE_URL = "http://backend:8000"

# Function to get the list of apartments
def get_listings():
    response = requests.get(f"{BASE_URL}/listings")
    if response.status_code == 200:
        return response.json()["apartments"]
    else:
        st.error(f"Error retrieving listings: {response.text}")
        return []

# Function to search for apartments
def search_apartments(search_form):
    response = requests.post(f"{BASE_URL}/search", json=search_form)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error searching for apartments: {response.text}")
        return []

# Function to add a new apartment
def add_new_apartment(new_apartment):
    response = requests.post(f"{BASE_URL}/addnew", json=new_apartment)
    if response.status_code == 200:
        return response.json()["new_listing"]
    else:
        st.error(f"Error adding new apartment: {response.text}")
        return None

# Streamlit UI
st.title("Apartment Management App")

# Get all apartments
all_apartments = get_listings()

# Display all apartments
st.header("List of Apartments")
st.write(all_apartments)

# Apartment Search Form
st.header("Search Apartments")
search_form = st.form(key="search_form")
min_price = search_form.number_input("Minimum Price", value=0)
max_price = search_form.number_input("Maximum Price", value=10000)
submit_search = search_form.form_submit_button("Search")

if submit_search:
    search_params = {"min_price": min_price, "max_price": max_price}
    search_results = search_apartments(search_params)
    st.write(search_results)

# Add New Apartment Form
st.header("Add New Apartment")
add_form = st.form(key="add_form")
new_apartment_name = add_form.text_input("Apartment Name")
new_apartment_price = add_form.number_input("Apartment Price")
submit_add = add_form.form_submit_button("Add Apartment")

if submit_add:
    new_apartment_info = {"name": new_apartment_name, "price": new_apartment_price}
    new_listing = add_new_apartment(new_apartment_info)
    if new_listing:
        st.success(f"New apartment added successfully: {new_listing}")

