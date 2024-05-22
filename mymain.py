from openai import OpenAI
import recorder
import config
from selenium import webdriver
import time

print("Please speak!\n")

recorder.record()

client = OpenAI(api_key=config.OPENAI_API_KEY)


audio_file = open("audio.mp3", "rb")
transcription = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file,
    response_format="text"
)

print("Your transcription reads:\n" + transcription + "\n")

print("Generating images based on your transcription...\n")

image = client.images.generate(
    prompt=transcription,
    n=2,
    size="1024x1024"
)

print(image.data[0].url)

driver = webdriver.Chrome()
driver.get(image.data[0].url)
time.sleep(60)
