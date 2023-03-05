
import streamlit as st
import openai
from streamlit_chat import message

st.title("Sentiment Analysis Demo")


readme = st.checkbox("readme first")

if readme:

    st.write("""
        This is a sentiment analysis demo using [ChatGPT API](https://openai.com/). 
        The web app is hosted on [streamlit cloud](https://streamlit.io/cloud). 
        You may get the codes [HERE](https://github.com/richieyuyongpoh/sentimentalAnalysis). 
        """)
    st.write ("For more info, please contact:")
    st.write("<a href='https://www.linkedin.com/in/yong-poh-yu/'>Dr. Yong Poh Yu </a>", unsafe_allow_html=True)
    
    
if 'messages' not in st.session_state:
    st.session_state['messages'] = [
            {"role": "system", "content": "Your name is Jane, Yong Poh's personal assistant. You are an expert who always provides consultation on sentimental analysis. For sentiment of a statement, You reply two words: sentimental type (positive, neutral, negative) and score (ranging from +1 to -1)"},
            {"role": "user", "content": "Fuck you! It is a bad day!"},
            {"role": "assistant", "content": "Sentiment: Negative  Score: -1"}]

openai.api_key = st.secrets["api_secret"] 

def generate_response(prompt):
  
    st.session_state['messages'].append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            max_tokens = 500,
            messages=st.session_state['messages']
        )
    st.session_state['messages'].append({"role": "assistant", "content": response["choices"][0]["message"].content})
    
    return response["choices"][0]["message"].content 
             
             
st.write("")
    # Storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []
             
def get_text():
    input_text = st.text_input("Chew Peng: ","Hello PP", key="input")
    return input_text
             
user_input = get_text()

if user_input:
    output = generate_response(user_input)
    # store the output  
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)
             
if st.session_state['generated']: 
    
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
