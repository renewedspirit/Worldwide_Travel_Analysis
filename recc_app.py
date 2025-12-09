import pandas as pd
import numpy as np
import streamlit as st

# In this file we'll be creating a tool using the Streamlit library,
# that takes a few user inputs (like budget or chosen continent),
# and get a recommended travel city.

# Page Configuration
st.set_page_config(
    page_title="Worldwide Travel Analysis",
    page_icon=":flight_departure:",
    layout="wide",
)


#  Load Data
@st.cache_data
def load_data():
    """Load data from a CSV file."""
    df = pd.read_csv("data/wtc_cleaned_dashboard_dataset.csv")
    return df


# Main App
df = load_data()
st.title("Worldwide Travel Analysis and Recommendation App :flight_departure:")
st.write(
    """
    This app recommends travel destinations based on user preferences such as budget, continent, and travel type.
    """
)


col1, col2 = st.columns([3, 7])

with col1:

    # User inputs
    st.header("User Input Features")

    b_options = df["budget_level"].unique().tolist()
    b_selection = st.pills("Select Budget", b_options, selection_mode="single")

    r_options = df["region"].unique().tolist()
    r_options = np.strings.capitalize(r_options)
    r_selection = st.pills("Select Region", r_options, selection_mode="single")

    t_length = st.selectbox(
        "Trip Length",
        ["All"] + sorted(
            [
                "Day Trip (1 Days)",
                "Weekend (2 Days)",
                "Short (3-6 Days)",
                "One Week (7 Days)",
                "Long Trip (8+ Days)",
            ]
        ),
    )

    city_features = df[df['culture', 'adventure', 'nature', 'beaches', 'nightlife', 'cuisine', 'wellness', 'urban', 'seclusion']].columns.tolist()

    feauture_pref = st.selectbox(
        "City Features", ["All"] + sorted(df["city_features"]))
