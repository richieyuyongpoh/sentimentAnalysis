
import streamlit as st
import openai


st.title("Sentiment Analysis Demo")


readme = st.checkbox("readme first")

if readme:

    st.write("""
        This is a sentiment analysis demo using [OpenAI API](https://openai.com/). 
        The web app is hosted on [streamlit cloud](https://streamlit.io/cloud). 
        You may get the codes [HERE](https://github.com/richieyuyongpoh/sentimentalAnalysis). 
        """)
    st.write ("For more info, please contact:")
    st.write("<a href='https://www.linkedin.com/in/yong-poh-yu/'>Dr. Yong Poh Yu </a>", unsafe_allow_html=True)
    
    
user_input = st.text_input("Enter your texts here:")
st.write ("Results:")
st.write("")

openai.api_key = st.secrets["API_KEY"] 

def analyze_sentiment(text):
    prompt = f"Get the sentiment(positive, neutral, negative) and score (between 1 to -1) of the following texts : {text}\n"
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        temperature=0)
    details = completions.choices[0].text
    
    return details

  
if user_input:
    details = analyze_sentiment(user_input)
    st.write(details)
   
else:
    st.write("Enter your texts first.")
