
from google import genai
from gtts import gTTS # google built in text to speech
import io #eta locally save er poriborte buffer create korbe ram e
from dotenv import load_dotenv
import os
load_dotenv()

api_key =  os.getenv("GEMINI_API_KEY")


client = genai.Client(api_key=api_key)


#note generator
def note_generator(images):
    prompt = """Summarize the content of the image in English within a maximum of 100 words. 
Write the summary in note format using bullet points. 
Use Markdown formatting with English section headings (e.g., ## Overview, ## Key Points) to clearly separate sections. 
Focus only on the most important information from the image."""

    response=client.models.generate_content(
         model="gemini-3-flash-preview",
         contents=[images,prompt]
    )

    return response.text


def  audio_transcription(text):
    speech  = gTTS(text,lang="en",slow=False)
    audio_buffer = io.BytesIO()

    speech.write_to_fp(audio_buffer)

    return audio_buffer


def quiz_generator(image,difficulty):

    prompt = f"Generate 3 quizzes based on the {difficulty}. Make sure to add markdown to differentiate the options. Add correct answer too,after the quiz"


    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents=[image,prompt]
    )

    return response.text 