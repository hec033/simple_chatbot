import os
from openai import OpenAI


def chatbot():
    # Load your API key from an environment variable or secret management service
    client = OpenAI(
        # This is the default and can be omitted
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    # create a list to store all messages for context
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
    ]

    # keep repeating the following
    while True:
        # prompt user
        message = input("User: ")

        # Exit program if user inputs "quit"
        if message.lower() == "quit":
            break

        # add each message to the list
        messages.append({"role": "user", "content": message})

        # request gpt-4-turbo-preview for chat completion
        completion = client.chat.completions.create(
            messages=messages,
            model="gpt-4-turbo-preview"
        )

        # print response and add it to the message list
        # chat_response = response
        chat_message = completion.choices[0].message.content
        print(f"Bot: {chat_message}")
        messages.append({"role": "assistant", "content": chat_message})
        print()


if __name__ == "__main__":
    print("Starting chatting with the bot (type 'quit' to stop)!")
    chatbot()
