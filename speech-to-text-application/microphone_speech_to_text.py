import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# listening the speech and store in audio_text variable
with sr.Microphone() as source:
    print("Talk")
    audio_text = r.listen(source)
    print("Time over, thanks")

    try:
        # using google speech recognition
        # print("Text:", r.recognize_google(audio_text))

        # Adding "hindi language"
        print("Text: ", r.recognize_google(audio_text, language="hi-IN"))
    except:
        print("Sorry, I did not get that")
