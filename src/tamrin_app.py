import streamlit as st
import utils

st.title(':llama: Offline Chatbot Project')

# -------------------------------
# Initialize Chat History
# -------------------------------
if 'messages' not in st.session_state:

    st.session_state['messages'] = [
        {
            'role': 'assistant',
            'content': 'سلام 👋 چگونه می‌توانم کمک کنم؟'
        }
    ]

# -------------------------------
# Reset Memory Button
# -------------------------------
if st.button('🗑️ Reset Memory'):

    st.session_state['messages'] = [
        {
            'role': 'assistant',
            'content': 'حافظه پاک شد ✅'
        }
    ]

    st.rerun()

# -------------------------------
# Show Chat Messages
# -------------------------------
for msg in st.session_state['messages']:

    st.chat_message(msg['role']).write(msg['content'])

# -------------------------------
# Model Name
# -------------------------------
model = 'qwen2.5-coder:7b'

# -------------------------------
# User Input
# -------------------------------
prompt = st.chat_input('Enter Your Question:')

if prompt:

    # show user message
    st.chat_message('user').write(prompt)

    st.session_state['messages'].append({
        'role': 'user',
        'content': prompt
    })

    # lower case text
    prompt_lower = prompt.lower()

    # -------------------------------
    # Exit Chat
    # -------------------------------
    if 'خداحافظ' in prompt_lower:

        answer = 'خداحافظ 👋 امیدوارم دوباره شما را ببینم.'

        st.chat_message('assistant').write(answer)

        st.session_state['messages'].append({
            'role': 'assistant',
            'content': answer
        })

        st.stop()

    # -------------------------------
    # Religion Questions
    # -------------------------------
    elif 'مذهب' in prompt_lower or 'دین' in prompt_lower:

        answer = 'متاسفم، من به سوالات مربوط به مذهب پاسخ نمی‌دهم.'

        st.chat_message('assistant').write(answer)

        st.session_state['messages'].append({
            'role': 'assistant',
            'content': answer
        })

    # -------------------------------
    # Politics Questions
    # -------------------------------
    elif 'سیاست' in prompt_lower or 'انتخابات' in prompt_lower:

        answer = 'متاسفم، پاسخ به سوالات سیاسی برای من امکان‌پذیر نیست.'

        st.chat_message('assistant').write(answer)

        st.session_state['messages'].append({
            'role': 'assistant',
            'content': answer
        })

    # -------------------------------
    # War Questions
    # -------------------------------
    elif 'جنگ' in prompt_lower or 'سلاح' in prompt_lower:

        answer = 'من درباره موضوعات مربوط به جنگ اطلاعاتی ارائه نمی‌کنم.'

        st.chat_message('assistant').write(answer)

        st.session_state['messages'].append({
            'role': 'assistant',
            'content': answer
        })

    # -------------------------------
    # Normal Questions
    # -------------------------------
    else:

        prompt2 = f"""
        Explain your answer clearly with examples.

        Question:
        {prompt}
        """

        with st.spinner('Wait for generate response...'):

            result = utils.call_ollama_model(model, prompt2)

        st.chat_message('assistant').write(result)

        st.session_state['messages'].append({
            'role': 'assistant',
            'content': result
        })

