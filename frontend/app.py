import streamlit as st

# Function to render the home page
def home():
    st.title("Listing Web App")
    st.write("Welcome to the Listing Web App. Use the navigation bar to explore different functionalities.")

# Function to render the "Add New" page
def add_new():
    st.title("Add New Item")
    # Add your code for adding new items here

# Function to render the "Search" page
def search():
    st.title("Search Items")
    # Add your code for searching items here

# Main function to run the Streamlit app
def main():
    st.title("Navigation Bar")

    # Use buttons for navigation
    nav_option = st.button("Home")
    if nav_option:
        home()

    nav_option = st.button("Add New")
    if nav_option:
        add_new()

    nav_option = st.button("Search")
    if nav_option:
        search()

# Run the app
if __name__ == "__main__":
    main()
