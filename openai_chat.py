import os
import openai


def send_message_to_openai(input_text):
    # Function to send a message to the OpenAI API and retrieve the response
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Initialize the OpenAI client with the API key from environment variables
    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # Specify the model/engine to use
            messages=[
                {"role": "user", "content": input_text}  # The input message to the OpenAI model
            ]
        )
        # Retrieve and return the text part of the response
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"  # Return the error message in case of an exception
