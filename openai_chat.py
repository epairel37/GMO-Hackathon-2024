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

def text_from_audio(input_file):
    print(config.OPENAI_API_KEY)
    client = openai.OpenAI(api_key=config.OPENAI_API_KEY)
    try:
        audio_file = open(input_file, "rb")
        # transcription from audio
        transcription = client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file, 
            response_format="text"
        )
        return transcription;
    except Exception as e:
        # Return the error message in case of an exception
        return f"Error: {str(e)}"

def generate_image(input_text):
    print(config.OPENAI_API_KEY)
    client = openai.OpenAI(api_key=config.OPENAI_API_KEY)
    try:
        # image from text
        image = client.images.generate(
            prompt=input_text,
            n=2,
            size="1024x1024"
        )
        # Retrieve and return the text part of the response
        return image.data[0].url;
    except Exception as e:
        # Return the error message in case of an exception
        return f"Error: {str(e)}"
