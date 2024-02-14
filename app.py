import streamlit as st
from openai import OpenAI


def app():
    st.title("Hex AI")

    client = OpenAI(api_key='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')

    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-4-turbo-preview"

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "system", "content": "You are Hex, an AI assistant. Answer as concisely as possible."}
        ]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Starting chatting with Hex (type 'quit' to stop)!"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            stream = client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ],
                stream=True,
            )
            response = st.write_stream(stream)
        st.session_state.messages.append({"role": "assistant", "content": response})


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app()
