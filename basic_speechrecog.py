import speech_recognition as sr

#initialise audio recogniser
audio_recogniser = sr.Recognizer()

#initialise audio source
with sr.Microphone() as source:
    print('Say something into the microphone!')
    #takes input from the source and stores it in audio variable
    audio = audio_recogniser.listen(source)

    try:
        #converts audio input into text and prints output
        voice_input = audio_recogniser.recognize_google(audio)
        print(f'You said: {voice_input}')
    except sr.UnknownValueError:
        print('Oops! I failed to recognise what you said')
    except sr.RequestError:
        print('Oops! Google Speech Recognition service is down')

