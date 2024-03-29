import streamlit as st
import openai
from streamlit_chat import message

st.title("Sentiment Analysis Demo")


readme = st.checkbox("readme first")

if readme:

    st.write("""
        This is a sentiment analysis demo using [ChatGPT API](https://openai.com/). 
        The web app is hosted on [streamlit cloud](https://streamlit.io/cloud). 
        """)
    st.write ("For more info, please contact:")
    st.write("<a href='https://www.linkedin.com/in/yong-poh-yu/'>Dr. Yong Poh Yu </a>", unsafe_allow_html=True)
    
st.write("Instruction:")
st.write("")

st.write("Type the statement in the following textbox. The AI assistant, Jane will give you the sentiment type and score.")

openai.api_key = st.secrets["api_secret"] 

def generate_response(prompt):
  
    init_messages = [
        {"role": "system", "content": "You only do sentiment analysis. For any statements provided by the users, You reply two words: sentiment type (positive, neutral, negative) and score (ranging from +1 to -1)"},
        {"role": "user", "content": "Fuck you! It is a bad day!"},
        {"role": "assistant", "content": "Sentiment: Negative ; Score: -1"},
        {"role": "user", "content": prompt}]
  
    response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            max_tokens = 500,
            messages= init_messages)

    return response["choices"][0]["message"].content 
             
             
st.write("")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []
             
def get_text():
    input_text = st.text_input("User: ","I am happy, Jane.", key="input")
    return input_text
             
user_input = get_text()

if user_input:
    output = generate_response(user_input)  
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)
             
if st.session_state['generated']: 
    
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
