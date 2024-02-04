import streamlit as st
import requests

# Function to fetch data from the "/listings" endpoint
def get_listings(page_number, items_per_page):
    url = f"http://localhost:8000/listings?page={page_number}&per_page={items_per_page}"  # Replace with the actual URL of your FastAPI app
    response = requests.get(url)
    return response.json()


# Streamlit app
def main():
    # Page configurations
    st.set_page_config(
        page_title="Listings Page",
        page_icon=":house:",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Sidebar - Navigation Bar
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Listings", "About"])

    if page == "Home":
        st.title("Welcome to the Home Page")
        st.write("This is the home page content.")

    elif page == "Listings":
        st.title("Listings Page")

        # Settings for pagination
        current_page = st.sidebar.number_input("Current Page", value=1, min_value=1)
        items_per_page = st.sidebar.number_input("Items Per Page", value=10, min_value=1, max_value=100)

        # Get listings
        all_listings = get_listings(current_page, items_per_page)

        # Render listings
        for listing in all_listings:
            st.write(listing)

        # Pagination
        st.sidebar.write("Page Navigation")
        st.sidebar.write(f"Current Page: {current_page}")
        st.sidebar.write(f"Total Items: {len(all_listings)}")

    elif page == "About":
        st.title("About Us")
        st.write("This is the about page content.")

    # Footer
    st.markdown(
        """
        ---\n
        © 2024 Your Company. All rights reserved.\n
        Contact us: contact@yourcompany.com
        """
    )

if __name__ == "__main__":
    main()