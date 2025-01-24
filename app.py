import streamlit as st

# Title and description
st.title("Personal Chatbot")
st.write("Chat with me! I'm here to answer your questions.")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input box
with st.form(key="chat_form", clear_on_submit=True):
    user_message = st.text_input("Type your message:")
    submit = st.form_submit_button("Send")

# Process user input
if submit and user_message:
    # Append user message to the session state
    st.session_state.messages.append({"role": "user", "content": user_message})
    
    # Generate a simple response (replace this with AI integration like OpenAI API)
    bot_response = f"You said: {user_message}. How can I assist further?"
    st.session_state.messages.append({"role": "bot", "content": bot_response})

# Display chat history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.write(f"**You:** {message['content']}")
    else:
        st.write(f"**Bot:** {message['content']}")
