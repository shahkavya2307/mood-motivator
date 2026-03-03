import os 
import requests
import streamlit as st





def mood(user_mood,user_name):

    gen_ai_key = st.secrets["GEMINI_API_KEY"]

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={gen_ai_key}"

    headers = {
        'Content-Type' : "application/json" 
    }


    payload = {
        "systemInstruction" : {
            "parts" : [
                {
                "text" : "You are good motivator . On any specific you will help the user to be happy .Talk in a easy english and give some bhagwad gita sholak and its translation with rest to mood and help the person to come out of this delima"
                }
            ]
        },
        "contents": [
            {
            "parts" : [
                            {
                                "text": f"I am feeling{user_mood}.Give me a short , classy motivational boost. and my name is {user_name}"
                            }
                        ]
            }
        ],
        "generationConfig" : {
            "temperature" : 0.7,
            "topP" : 0.95,
        }

    }


    response = requests.post(url,headers=headers,json=payload)

    if response.status_code == 200:
        data = response.json()  

        mood_message = data['candidates'][0]['content']['parts'][0]['text']

        return mood_message
    else:

        return "Oops!"





