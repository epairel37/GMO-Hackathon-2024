import openai
import config


def send_message_to_openai(input_text):
    # Function to send a message to the OpenAI API and retrieve the response
    # Initialize the OpenAI client with the API key from environment variables
    print(config.OPENAI_API_KEY)
    client = openai.OpenAI(api_key=config.OPENAI_API_KEY)
    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # Specify the model/engine to use
            messages=[
                # The input message to the OpenAI model
                {"role": "user", "content": input_text}
            ]
        )
        # Retrieve and return the text part of the response
        return response.choices[0].message.content.strip()
    except Exception as e:
        # Return the error message in case of an exception
        return f"Error: {str(e)}"
