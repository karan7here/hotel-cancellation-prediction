import streamlit as st
import pandas as pd
import numpy as np
import joblib

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Hotel Cancellation Prediction",
    page_icon="🏨",
    layout="wide"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

.main {
    background-color: #f5f7fa;
}

h1 {
    color: #ff4b4b;
    text-align: center;
}

.stButton>button {
    background-color: #ff4b4b;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
    font-weight: bold;
}

.css-1d391kg {
    background-color: #ffffff;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# LOAD MODEL & SCALER
# =====================================================

model = joblib.load("hotel_reservation_model.pkl")
scaler = joblib.load("scaler.pkl")

# =====================================================
# TITLE
# =====================================================

st.title("🏨 Hotel Reservation Cancellation Prediction")

st.markdown("---")

st.write(
    "This Machine Learning application predicts whether a hotel reservation will be cancelled or not."
)

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.header("Enter Booking Details")

# =====================================================
# INPUTS
# =====================================================

no_of_adults = st.sidebar.number_input(
    "Number of Adults",
    min_value=1,
    max_value=10,
    value=2
)

no_of_children = st.sidebar.number_input(
    "Number of Children",
    min_value=0,
    max_value=10,
    value=0
)

no_of_weekend_nights = st.sidebar.number_input(
    "Weekend Nights",
    min_value=0,
    max_value=10,
    value=1
)

no_of_week_nights = st.sidebar.number_input(
    "Week Nights",
    min_value=0,
    max_value=20,
    value=2
)

required_car_parking_space = st.sidebar.selectbox(
    "Parking Required",
    [0, 1]
)

lead_time = st.sidebar.number_input(
    "Lead Time",
    min_value=0,
    max_value=500,
    value=50
)

arrival_year = st.sidebar.selectbox(
    "Arrival Year",
    [2017, 2018]
)

arrival_month = st.sidebar.selectbox(
    "Arrival Month",
    list(range(1, 13))
)

arrival_date = st.sidebar.selectbox(
    "Arrival Date",
    list(range(1, 32))
)

repeated_guest = st.sidebar.selectbox(
    "Repeated Guest",
    [0, 1]
)

no_of_previous_cancellations = st.sidebar.number_input(
    "Previous Cancellations",
    min_value=0,
    max_value=20,
    value=0
)

no_of_previous_bookings_not_canceled = st.sidebar.number_input(
    "Previous Non-Cancelled Bookings",
    min_value=0,
    max_value=50,
    value=0
)

avg_price_per_room = st.sidebar.number_input(
    "Average Price Per Room",
    min_value=0.0,
    max_value=10000.0,
    value=100.0
)

no_of_special_requests = st.sidebar.number_input(
    "Special Requests",
    min_value=0,
    max_value=10,
    value=1
)

# =====================================================
# CATEGORICAL FEATURES
# =====================================================

meal_plan = st.sidebar.selectbox(
    "Meal Plan",
    ['Meal Plan 1', 'Meal Plan 2', 'Meal Plan 3', 'Not Selected']
)

room_type = st.sidebar.selectbox(
    "Room Type",
    ['Room_Type 1', 'Room_Type 2', 'Room_Type 3',
     'Room_Type 4', 'Room_Type 5', 'Room_Type 6',
     'Room_Type 7']
)

market_segment = st.sidebar.selectbox(
    "Market Segment",
    ['Online', 'Offline', 'Corporate',
     'Complementary', 'Aviation']
)

# =====================================================
# MANUAL ENCODING
# =====================================================

meal_map = {
    'Meal Plan 1': 0,
    'Meal Plan 2': 1,
    'Meal Plan 3': 2,
    'Not Selected': 3
}

room_map = {
    'Room_Type 1': 0,
    'Room_Type 2': 1,
    'Room_Type 3': 2,
    'Room_Type 4': 3,
    'Room_Type 5': 4,
    'Room_Type 6': 5,
    'Room_Type 7': 6
}

market_map = {
    'Online': 0,
    'Offline': 1,
    'Corporate': 2,
    'Complementary': 3,
    'Aviation': 4
}

meal_plan = meal_map[meal_plan]
room_type = room_map[room_type]
market_segment = market_map[market_segment]

# =====================================================
# FEATURE ENGINEERING
# =====================================================

total_guests = no_of_adults + no_of_children

total_nights = no_of_weekend_nights + no_of_week_nights

# =====================================================
# CREATE INPUT DATAFRAME
# =====================================================

input_data = pd.DataFrame({
    'no_of_adults': [no_of_adults],
    'no_of_children': [no_of_children],
    'no_of_weekend_nights': [no_of_weekend_nights],
    'no_of_week_nights': [no_of_week_nights],
    'type_of_meal_plan': [meal_plan],
    'required_car_parking_space': [required_car_parking_space],
    'room_type_reserved': [room_type],
    'lead_time': [lead_time],
    'arrival_year': [arrival_year],
    'arrival_month': [arrival_month],
    'arrival_date': [arrival_date],
    'market_segment_type': [market_segment],
    'repeated_guest': [repeated_guest],
    'no_of_previous_cancellations': [no_of_previous_cancellations],
    'no_of_previous_bookings_not_canceled': [no_of_previous_bookings_not_canceled],
    'avg_price_per_room': [avg_price_per_room],
    'no_of_special_requests': [no_of_special_requests],

    # NEW FEATURES
    'total_guests': [total_guests],
    'total_nights': [total_nights]
})

# =====================================================
# SCALE INPUT
# =====================================================

input_scaled = scaler.transform(input_data)

# =====================================================
# PREDICTION
# =====================================================

if st.button("Predict Booking Status"):

    prediction = model.predict(input_scaled)

    probability = model.predict_proba(input_scaled)

    st.markdown("---")

    if prediction[0] == 1:

        st.error("❌ Booking Will Likely Be Cancelled")

    else:

        st.success("✅ Booking Will Likely Not Be Cancelled")

    st.subheader("Prediction Probability")

    st.write(
        f"Cancellation Probability: {probability[0][1] * 100:.2f}%"
    )

    st.write(
        f"Non-Cancellation Probability: {probability[0][0] * 100:.2f}%"
    )

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.caption("Developed using Streamlit & Machine Learning")