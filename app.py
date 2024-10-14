from openai import OpenAI
import config

client = OpenAI(api_key=config.api_key)

messages = [
    {"role": "system", "content": "Eres un asistente util"}
    ]
userin = input("Pregunta: ")

messages.append({"role": "user", "content": userin})

completion = client.chat.completions.create(
    model= "gpt-3.5-turbo",
    messages= messages
)

assistant_response = completion.choices[0].message.content
print(f"assistant: {assistant_response}")
