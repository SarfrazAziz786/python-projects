import streamlit as st  # for web interface and uv add streamlit and pandas install command
import pandas as pd  #for data manipulation
import datetime
import csv #csv format read and write
import os # for file operations

# uppercase file name for constant variables
MOOD_FILE = "mood_log.csv"


def load_mood_data():  #function to read data from the csv file
    
    if not os.path.exists(MOOD_FILE):
        return pd.DataFrame(columns=["Date", "Mood"])   #for specific formatting framework and if file not exists so create 2 columns date and mood in the file
    
    return  pd.read_csv(MOOD_FILE)

def save_mood_data(date , mood): #new mood entries
    with open(MOOD_FILE , 'a') as file: # for resources management data add functionality
        
        writer = csv.writer(file)        
        
        writer.writerow([date, mood]) #store data by row

st.title("Mood Tracker")

today = datetime.date.today() 

st.subheader("How are you feeling today")

mood = st.selectbox("Select your mood", ["Sad", "Neutral", "Happy", "Excited"])

if st.button("Log Mood"):
    save_mood_data(today, mood)
    st.success("Mood logged successfully!")

#create a session for visualization
data = load_mood_data()


if not data.empty: 
    st.subheader("Mood Trends over time")
    
    data["Date"] = pd.to_datetime(data["Date"]) #convert date string to datetime object

    mood_counts = data.groupby("Mood").count()["Date"]

    st.bar_chart(mood_counts)

