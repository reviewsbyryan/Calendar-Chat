import speech_recognition as sr

def recognize_speech():
    """Recognizes speech from the microphone."""
    # Initialize the speech recognizer
    r = sr.Recognizer()

    # Start recording audio
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # Transcribe the audio
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)
    except sr.UnknownValueError:
        print("I could not understand what you said.")

    return text