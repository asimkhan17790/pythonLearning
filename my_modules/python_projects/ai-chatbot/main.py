from openai import OpenAI

client = OpenAI()
messages = [
    {"role": "developer",
     "content": "Talk formally and very concise"
     }
]


def completion(message):
    global messages
    print("CONTEXT: ", messages)
    # Add latest user input to message context
    messages.append({"role": "user",
                     "content": message
                     })

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-5"
    )
    # print(chat_completion)

    message = {
        "role": "assistant",
        "content": chat_completion.choices[0].message.content
    }
    # Adding context at line 29
    messages.append(message)
    print(f"Jarvis: {message["content"]}")


if __name__ == "__main__":
    print(f"Jarvis: Hi, I am Jarvis... How can I help you?")
    while True:
        user_question = input(f"Your Query: ")
        print("User:", user_question)
        completion(user_question)
