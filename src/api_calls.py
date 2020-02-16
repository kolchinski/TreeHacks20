import cv2
import simpleaudio as sa

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
from google.cloud import texttospeech

def text_from_image(image):
    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    image = types.Image(content=cv2.imencode('.jpg', image)[1].tostring())

    response = client.text_detection(image=image)
    full_text = response.full_text_annotation.text
    return full_text


def read_text(text):
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.types.SynthesisInput(text=text)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

    # Select the type of audio file you want returned
    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.LINEAR16)

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(synthesis_input, voice, audio_config)
    audio = response.audio_content
    play_obj = sa.play_buffer(audio, 1, 2, 22050)

