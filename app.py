from flask import Flask, request, jsonify
from openai import OpenAI
import config

app = Flask(__name__)

# Configura el API cliente de OpenAI
client = OpenAI(api_key=config.api_key)

# Asigna un rol especifico al sistema
messages = [
    {"role": "system", "content": "Eres un asistente útil"}
]

@app.route('/chatgpt', methods=['POST'])
def chatgpt():
    # Extrae la consulta del cuerpo de la solicitud
    data = request.json
    content = data.get('query')

    # Agrega la consulta del usuario a la lista de mensajes
    messages.append({"role": "user", "content": content})

    try:
        # Realiza la solicitud a la API de OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        # Obtén el contenido de la respuesta
        response_content = response.choices[0].message.content

        # Agrega la respuesta del asistente a la lista de mensajes
        messages.append({"role": "assistant", "content": response_content})

        # Devuelve la respuesta en formato JSON
        return jsonify({'response': response_content})
    except Exception as e:
        # Devuelve un mensaje de error en caso de fallo
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
