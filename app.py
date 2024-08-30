import requests
import streamlit as st
from datetime import datetime



# Streamlit form for user inputs
st.title("NY Taxi Fare Prediction")

# Date and time
date = st.date_input("Pick a date", datetime.today())
time = st.time_input("Pick a time", datetime.now().time())

# Pickup and dropoff coordinates
pickup_longitude = st.number_input("Pickup Longitude", value=-73.985428)
pickup_latitude = st.number_input("Pickup Latitude", value=40.748817)
dropoff_longitude = st.number_input("Dropoff Longitude", value=-73.985428)
dropoff_latitude = st.number_input("Dropoff Latitude", value=40.748817)

# Passenger count
passenger_count = st.number_input("Passenger Count", min_value=1, max_value=6, value=1)


url = 'https://taxifare.lewagon.ai/predict'




# Combine date and time
pickup_datetime = f"{date} {time}"

# Create a dictionary for the API parameters
params = {
    "pickup_datetime": pickup_datetime,
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}

# Make the API call
if st.button("Predict Fare"):
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        prediction = response.json()["fare"]
        st.success(f"The predicted fare is: ${prediction:.2f}")
    else:
        st.error("Error in API call. Please try again.")
