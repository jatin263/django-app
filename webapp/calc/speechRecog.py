import speech_recognition as sr
r = sr.Recognizer()
def speechToText(s):
    with sr.AudioFile(s) as source:
        audio_text = r.listen(source)
        try:
            # using google speech recognition
            text = r.recognize_google(audio_text)
            print('Converting audio transcripts into text ...')
            return text
        except:
            return 'Sorry.. run again...'