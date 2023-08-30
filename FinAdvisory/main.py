import streamlit as st
import helper
from fetchstockinfo import Anazlyze_stock
import openai
st.title("🦜🔗Financial Advisory-GPT")
st.write("This bot scraps and gathers real time stock related information using OpenAI & Yahoo Finance and analyzes it using LLM and Langchain")

query = st.text_input('Input the Company name to be advised')

Enter=st.button("Analyze")

if Enter:
    import time
    with st.spinner('Gathering all required information and analyzing. Be patient!!!!!'):
        out=Anazlyze_stock(query)
        st.success('Done!')
        st.write(out)

# securities = st.sidebar.selectbox("Select your securities type", ("Stocks", "Mutual Funds"))
#
# with st.sidebar:
#     if securities:
#         response = helper.generate_advisory(securities)
#         menu_items = response['fund_name'].strip().split(",")
#         st.write("**Investment Plans**")
#         for item in menu_items:
#             st.write("-", item)

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
st.title("💬 Chatbot")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hey!, How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    openai.api_key = openai_api_key
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)
