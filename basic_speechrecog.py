import speech_recognition as speech
from googletrans import Translator

#initialise audio recogniser
audio_recogniser = speech.Recognizer()

#initialise translator
translator = Translator()

#initialise audio source
with speech.Microphone() as source:
    print('Say something into the microphone!')
    #takes input from the source and stores it in audio variable
    audio = audio_recogniser.listen(source)

    try:
        #converts audio input into text and prints original and translated output
        voice_input = audio_recogniser.recognize_google(audio)
        translated_input = translator.translate(voice_input, src = 'en', dest = 'it')
        print(f'You said: {voice_input}')
        print(f'This is "{translated_input.text}" in Italian!')
    except speech.UnknownValueError:
        print('Oops! I failed to recognise what you said')
    except speech.RequestError:
        print('Oops! Google Speech Recognition service is down')

