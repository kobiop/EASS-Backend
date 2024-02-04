import streamlit as st
import requests

def get_listings():
    url = "http://localhost:8000/"  # Replace with the actual URL of your FastAPI app
    response = requests.get(url)
    
    return response.json()

def user_preferences_form():
    st.title("User Preferences")

    location = st.text_input("Location")
    
    st.subheader("Property Type")
    property_types = st.multiselect("Select property types", ["Single family", "Condo", "Townhome", "Multi-Family"])

    st.subheader("Price Range")
    min_price = st.selectbox("Min Price", [0, 50000, 120000, 200000, 270000, 350000])
    max_price = st.selectbox("Max Price", [0, 50000, 120000, 200000, 270000, 350000])

    st.subheader("Bedrooms Range")
    min_bedrooms = st.selectbox("Min Bedrooms", [0, 1, 2, 3, 4, 5])
    max_bedrooms = st.selectbox("Max Bedrooms", [0, 1, 2, 3, 4, 5])

    st.subheader("Bathrooms Range")
    min_bathrooms = st.selectbox("Min Bathrooms", [0, 1, 2, 3, 4, 5])
    max_bathrooms = st.selectbox("Max Bathrooms", [0, 1, 2, 3, 4, 5])

    st.subheader("HOA Fees")
    hoa_fees_type = st.selectbox("Select HOA Fees Type", ["Any", "No HOA", "Select max HOA"])
    max_hoa_fees = st.selectbox("Max HOA Fees", [100, 200, 300, 400, 500], key="max_hoa_fees")

    st.subheader("Sqft Range")
    min_sqft = st.selectbox("Min Sqft", [0, 500, 750])
    max_sqft = st.selectbox("Max Sqft", [0, 1000, 1250])

    st.subheader("Sqft Lot Range")
    min_sqft_lot = st.selectbox("Min Sqft Lot", [0, 2000, 3000])
    max_sqft_lot = st.selectbox("Max Sqft Lot", [0, 4000, 5000])

    st.subheader("Min Built Year")
    min_home_age = st.selectbox("Min Built Year", [0, 1970, 1980])

    st.subheader("Garage")
    garage_options = ["Attached", "Detached", "None"]
    selected_garage = st.multiselect("Select Garage", garage_options)

    st.button("Save Preferences")

if __name__ == "__main__":
    user_preferences_form()
