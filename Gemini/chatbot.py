import pathlib
import textwrap
import google.generativeai as genai

# Replace with your method to retrieve the API key securely
GOOGLE_API_KEY = "AIzaSyCKaLXnrCVZz8uXqxGr0o-6kttDqt57PgA"
# Historial de conversación
conversation_history = []

def generate_response(question, context=None):
    try:
        genai.configure(api_key=GOOGLE_API_KEY)
        model = genai.GenerativeModel('gemini-pro')

        # Combinar la pregunta actual con el contexto anterior si está disponible
        if context:
            combined_input = f"{context} {question}"
        else:
            combined_input = question

        response = model.generate_content(combined_input)

        # Acceder al texto de la respuesta desde el objeto de respuesta
        generated_text = response.text

        # Actualizar el historial de la conversación
        conversation_history.append((question, generated_text))

        return generated_text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def print_conversation_history():
    print("Historial de la conversación:")
    for i, (question, answer) in enumerate(conversation_history, start=1):
        print(f"Pregunta {i}: {question}")
        print(f"Respuesta {i}: {answer}\n")

# Bucle principal de la conversación
while True:
    pregunta = input("Pregúntame lo que quieras o dime 'adios' para salir: ")

    if pregunta.lower() == "adios":
        break

    # Obtener la última respuesta generada como contexto
    contexto = conversation_history[-1][1] if conversation_history else None

    # Generar una respuesta para la pregunta actual
    respuesta_generada = generate_response(pregunta, contexto)

    if respuesta_generada:
        print(textwrap.indent(respuesta_generada, '> ', predicate=lambda _: True))

# Imprimir el historial de la conversación al finalizar
print_conversation_history()
print("¡Hasta luego!")