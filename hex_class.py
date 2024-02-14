import os
from openai import OpenAI


class HexAI:
    def __init__(self, open_ai_key, model, system_context, messages):
        self.client = OpenAI(
            # This is the default and can be omitted
            api_key=open_ai_key
        )
        self.model = "gpt-4-turbo-preview"
        self.system_context = {"role": "system", "content": {system_context}}
        self.messages = [system_context]

    def get_response(self, user_input):

        # Add user input to context messages
        self.messages.append({"role": "user", "content": user_input})

        # Get stream completion from OpenAI model
        stream_completion = self.client.chat.completions.create(
            messages=self.messages,
            model=self.model,
            stream=True
        )

        # Return stream
        return stream_completion




def hex_ai():
    # Load your API key from an environment variable or secret management service
    client = OpenAI(
        # This is the default and can be omitted
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    # create a list to store all messages for context
    messages = [
        {"role": "system", "content": "You are Hex, an AI assistant. Answer as concisely as possible."},
    ]

    # keep repeating the following
    while True:
        # prompt user
        message = input("User: ")

        # Exit program if user inputs "quit"
        if message.lower() in ["quit", "quit()", "stop", "stop()"]:
            break

        # add each message to the list
        messages.append({"role": "user", "content": message})

        # request gpt-4-turbo-preview for chat completion
        stream_completion = client.chat.completions.create(
            messages=messages,
            model="gpt-4-turbo-preview",
            stream=True
        )

        # print response and add it to the message list
        print("Hex: ", end="")
        entire_message = ""
        for chunk in stream_completion:
            msg = chunk.choices[0].delta.content or ""
            print(chunk.choices[0].delta.content or "", end="")
            entire_message += msg

        # add the bot response to messages
        messages.append({"role": "assistant", "content": entire_message})
        print()


if __name__ == "__main__":
    print("Starting chatting with Hex (type 'quit' to stop)!")
    hex_ai()
