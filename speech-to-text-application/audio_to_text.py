import speech_recognition as sr
import config

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# listening the audio file and store in audio_text variable
with sr.AudioFile(config.GLOBAL_SOUND_PATH + "audio_files_harvard.wav") as source:
    audio_text = r.listen(source)
    try:
        # using google speech recognition
        text = r.recognize_google(audio_text)
        print("Converting audio transcripts into text ...")
        print(text)
    except:
        print("Sorry.. run again...")
