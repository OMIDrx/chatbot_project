import streamlit as st
import time

prompt = st.chat_input('Enter your qustion?')
if prompt:
    st.write(f'OK: your qustion is: {prompt}')

messege = st.chat_message('ai').write('How can i help you')
messege_user = st.chat_message('user').write('who is ronaldo') #human


#with st.spinner('wait for answer...'):
#    time.sleep(6)
#st.write('Done')

# counter = 0
# if st.button('ADD'):
#     counter += 1
#     st.write(f'counter: {counter}')

st.write(f'session_state: {st.session_state}')
if 'counter' not in st.session_state:
    st.session_state['counter'] = 0

if st.button('ADD'):
    st.session_state['counter'] += 1
    st.write(f"counter: {st.session_state ['counter']}")
    