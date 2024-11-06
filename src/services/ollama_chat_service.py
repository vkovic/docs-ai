from ollama import Client


def chat() -> str:
    client = Client(host='ollama:11434')

    response = client.chat(model='llama3.2', messages=[
        {
            'role': 'user',
            'content': 'Tell me a joke',
        },
    ])

    return response['message']['content']
    
    
    







