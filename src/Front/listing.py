import streamlit as st
import requests

# Function to fetch data from the "/listings" endpoint
def get_listings():
    url = "http://localhost:8000/listings"  # Replace with the actual URL of your FastAPI app
    response = requests.get(url)
    return response.json()

# Custom CSS styles
custom_styles = """
    body {
        background-color: #f4f4f4;
        font-family: 'Arial', sans-serif;
    }
    .streamlit-title {
        color: #333333;
    }
    .streamlit-markdown-text-container {
        color: #555555;
    }
    .pagination-bar {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    .pagination-item {
        margin: 0 10px;
        cursor: pointer;
    }
"""

# Streamlit app
def main():
    # Apply custom styles
    st.markdown(f'<style>{custom_styles}</style>', unsafe_allow_html=True)

    st.title("Apartment Listings")

    # Fetch data from the "/listings" endpoint
    all_listings = get_listings()

    # Paginate the listings with 9 listings per page
    items_per_page = 9
    total_pages = (len(all_listings) // items_per_page) + 1
    current_page = st.session_state.get("current_page", 1)

    # Display the data in a 3x3 grid using styled cards
    columns = st.columns(3)  # Create three columns

    for i, listing in enumerate(all_listings[(current_page - 1) * items_per_page : current_page * items_per_page]):
        # Display each listing as a card in the grid
        with columns[i % 3]:
            st.markdown(
                f"**Apartment {listing['id']}**\n\n"
                f"**Address:** {listing['address']}\n"
                f"**Price:** ${listing['price']}\n"
                f"**Bedrooms:** {listing['beds']}\n"
                f"**Bathrooms:** {listing['bathrooms']}\n"
                f"**Area:** {listing['sqft']} sq. ft."
            )

    # Pagination bar below the apartments
    st.markdown('<div class="pagination-bar">', unsafe_allow_html=True)
    for page in range(1, total_pages + 1):
        button_clicked = st.button(f"Page {page}", key=f"button_{page}")
        if button_clicked:
            st.session_state["current_page"] = page
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
