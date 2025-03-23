import streamlit as st

st.title("Unit Converter 🌎")

st.markdown("### Convert Length , Weight and Time")
st.write("Welcome Select a Category, enter a value and get the converted result")

category = st.selectbox("Choose a Category", ["Length", "Weight", "Time"])   

def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
        
    elif category == "Weight":
            if unit == "Kilograms to Pounds":
                return value * 2.20462
            elif unit == "Pounds to Kilograms":
                return value / 2.20462
            
    elif category == "Time":
            if unit == "Seconds to Minutes":
                return value / 60  
            elif unit == "Minutes to Seconds":
                return value * 60
            elif unit == "Minutes to Hours":
                return value / 60  
            elif unit == "Hours to Minutes":
                return value * 60  
            elif unit == "Hours to Days":
                return value / 24
            elif unit == "Days to Hours":
                return value * 24
    return 0
            
if category == "Length":
    unit = st.selectbox("📏Select  Conversation", ["Miles to Kilometers", "Kilometers to Miles" ])

elif category == "Weight":
    unit = st.selectbox("⚖️Select  Conversation", ["Pounds to Kilograms","Kilograms to Pounds"])

elif category == "Time":
    unit = st.selectbox("⏱Select  Conversation", ["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Minutes", "Hours to Days", "Days to Hours"])

value = st.number_input("Enter the Value to Convert")

if st.button ("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"The result is {result:.2f}")  #2f is used to display the result upto 2 decimal places

