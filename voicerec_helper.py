import speech_recognition as sr


def rec_audio_response(question):
    ##declaring recognizer to work through application
    r = sr.Recognizer()
    
    ##Using Google Voice Recognition to try to pull audio
    with sr.Microphone() as source:
        print question
        audio = r.listen(source)
    try:
        print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    audio = r.recognize_google(audio)

    return audio
    
    
