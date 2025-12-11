import pandas as pd
import streamlit as st
import plotly.graph_objects as go

# In this file we'll be creating a tool using the Streamlit library,
# that takes a few user inputs (like budget or chosen continent),
# and get a recommended travel city.


# Instead of loading the data every time the app reruns,
# we can cache the data loading function.
@st.cache_data
def load_data():
    df = pd.read_csv("data/wtc_cleaned_dashboard_dataset.csv")
    return df


# Page Configuration
st.set_page_config(
    page_title="Wotrav",
    page_icon=":flight_departure:",
    layout="wide",
)

df_raw = load_data()
df = df_raw.copy()

feature_cols = [
    "culture", "adventure", "nature", "beaches", "nightlife",
    "cuisine", "wellness", "urban", "seclusion"
]

# App Title and Description
st.title("Wotrav :flight_departure:")
st.write(
    """
    Get the best travel suggestions with Wotrav. We recommend amazing cities that are personalised to your own preferences.
    Just select your budget, region, and trip duration, and you've got your next 3 travel destinations.
    This app is based on the Worldwide Travel Cities Dataset.
    """
)


# Layout: Two Columns
col1, col2 = st.columns([3, 7], border=True)

# User Input Section
with col1:

    # User inputs
    budget = st.pills("Select Budget", ["No Budget"] + df["budget_level"].unique().tolist())
    region = st.pills("Select Region", ["Any Region"] + df["region"].str.capitalize().unique().tolist())
    trip_length = st.selectbox(
        "Trip Length", ["All"] + sorted(["is_day_trip", "is_weekend", "is_short_trip",
                                         "is_one_week", "is_long_trip"]),)
    st.markdown(
        """
         **Instructions:**
        - Select your budget level.
        - Choose a region.
        - Specify your preferred trip length.
        
        Then the app will recommend the top travel destinations based on your inputs.
        """
    )


# Filter Data Based on User Inputs
def filter_cities(df, budget, region, trip_length):

    if budget != "No Budget":  # if something other than No Budget is selected then filter by the chosen budget
        df = df[df["budget_level"] == budget]

    if region != "Any Region":  # if something other than Any Region is selected then filter by the chosen region
        df = df[df["region"].str.capitalize() == region]

    if trip_length != "All":  # if something other than All is selected then filter by the chosen trip length
        df = df[df[trip_length] == 1]

    return df


filtered = filter_cities(df, budget, region, trip_length)  # calls the filter_cities to create a filtered dataFrame

if filtered.empty:  # if no cities match the criteria, the app shows an error message and stops execution
    st.error("No cities match your criteria. Try adjusting your filters.")
    st.stop()

filtered = filtered.sort_values("city_rating", ascending=False)
filtered["top_feature"] = filtered[feature_cols].idxmax(axis=1)  # identifies the top feature for each city and adds it as a new 'top_feature' column

top3 = filtered.head(3)

# Extracts Top 3 Cities, but handles cases where there are less than 3 cities
top = top3.iloc[0] if len(top3) >= 1 else None
second = top3.iloc[1] if len(top3) >= 2 else None
third = top3.iloc[2] if len(top3) >= 3 else None

# Visualization: Radar Chart for Top Recommended City
with col2:
    fig = go.Figure()

    # plots the radar chart for the top 3 recommended cities if they exist
    if len(top3) >= 1:
        fig.add_trace(go.Scatterpolar(
            r=top3[feature_cols].iloc[0].values,
            theta=feature_cols,
            fill='toself',
            name=f'1 - {top["city"]}'
        ))

    if len(top3) >= 2:
        fig.add_trace(go.Scatterpolar(
            r=top3[feature_cols].iloc[1].values,
            theta=feature_cols,
            fill='toself',
            name=f'2 - {second["city"]}'
        ))

    if len(top3) >= 3:
        fig.add_trace(go.Scatterpolar(
            r=top3[feature_cols].iloc[2].values,
            theta=feature_cols,
            fill='toself',
            name=f'3 - {third["city"]}'
        ))

    # Updates the layout of the radar chart, including size, title, range and theme
    fig.update_layout(
        width=800,
        height=600,
        polar=dict(  # polar is used to set the properties of the radar chart
            radialaxis=dict(
                range=[0, 6])),
        title="Comparison of Your Top 3 Recommended Cities",
        template="plotly_dark"
        )
    st.plotly_chart(fig)

# Displays the details of the top 3 recommended cities if they exist
if len(top3) >= 1:
    st.markdown("---")
    st.subheader(f"🌍 Top Destination: {top['city']}, {top['country']}")
    st.write(f'Your top recommended city is {top["city"]} in {top["country"]}.')
    st.write(f'{top["city"]} is known for its {top["top_feature"]}, and has an overall travel rating of {top["city_rating"]}.')
    st.write(f'It is best described as: {top["short_description"]}')

if len(top3) >= 2:
    st.markdown("---")
    st.subheader(f"🌍 Second Destination: {second['city']}, {second['country']}")
    st.write(f'Your second recommended city is {second["city"]} in {second["country"]}')
    st.write(f'{second["city"]} is known for its {second["top_feature"]}, and has an overall rating of {second["city_rating"]}.')
    st.write(f'It is best described as: {second["short_description"]}')

if len(top3) >= 3:
    st.markdown("---")
    st.subheader(f"🌍 Third Destination: {third['city']}, {third['country']}")
    st.write(f'Your third recommended city is {third["city"]} in {third["country"]}')
    st.write(f'{third["city"]} is known for its {third["top_feature"]}, and has an overall rating of {third["city_rating"]}.')
    st.write(f'It is best described as: {third["short_description"]}')

st.markdown("---")

st.expander("See Filtered dataset").dataframe(filtered)  # Shows the filtered dataset

# Downloads filtered data as CSV
csv = filtered.to_csv(index=False)
st.download_button(
    label="Download Filtered Data",
    data=csv,
    file_name="filtered_travel_destinations.csv",
    mime="text/csv",
    )
