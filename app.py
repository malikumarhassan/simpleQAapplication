# Import necessary libraries
from langchain.llms import OpenAI
import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")






# streamlit app UI part

st.set_page_config(page_title="Simple QA from OpenAI", page_icon=":robot:")
st.header("QA from OpenAI")
st.markdown("Ask a question and get an answer from OpenAI's GPT-3.5-turbo-instruct model.") 

#  Input text box for user question
def load_answer(question):
    answer = ""
    try:        
        llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0,api_key= OPENAI_API_KEY)
        answer = llm.invoke(question)       
    except Exception as ex:
        answer = "❌ Exception occurred while calling OpenAI: " + str(ex)
    finally:
        return answer

def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text  


user_input = get_text()
response = load_answer(user_input)

submit = st.button("Generate")

# Display the response if the user has submitted a question
if submit:
    st.subheader("Answer:")
    st.write(response)