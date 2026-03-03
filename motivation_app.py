import streamlit as st
from fetch_motivation import mood


st.title("Classy MoodResidue Motivator by Kavya_Shah")

user_name = st.text_input("Your Name" , placeholder="Type here...." ) #label,placeholder


user_mood = st.selectbox(
    "Pls select how you feel right now",#Question 
             [
                 "😂 Happy Always",
                 "😔 Sorry to hear",
                 "😩 Stressed",
                 "🥱 Tired and sleepy."
              ])

if st.button("Lets have a talk 😊"):

    if user_name:#check username is there or not
        mood_instructor = mood(user_mood,user_name)

        st.write(mood_instructor)
    
    else:
        st.warning("Please enter your name first!")


