import streamlit as st 

from groq import Groq

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.title("My chatbot🤖")

st.markdown("---")

st.title ("تحدث بدلا من الكتابه ")

audio=st.audio_input("سجل سؤالك...")

prompt= st.chat_input("اكتب سؤالك هنا")


if "messages" not in st.session_state:
    st.session_state.messages=[]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt:
    st.session_state.messages.append({"role":"user", "content" : prompt})
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assisiant"):
        with st.spinner("Thinking"):
            try:
                messages=[{"rule" : "system" , "content" : "You are a helpful assisiant"}]
                for msg in st.session_state.messages:
                    messages.append({"role" : msg["role"] , "content" : msg["content"]})
                response = client.chat.completions.create(
                    model ="openai/gpt-oss-120b",
                    messages=messages,
                    max_tokens=1000,
                    tempreture=0.7
                )
                ansewr= response.choices[0].message.content
            except Exception as e:
                ansewr=e
        st.write(ansewr)
    st.session_state.messages.append({"role" : "assisiant" , "content" : ansewr})
