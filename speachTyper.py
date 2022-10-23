import speech_recognition as sr
from PyQt5.QtCore import *
import datetime


class speachTyper(QThread) :
    typeSpeachResultSignal = pyqtSignal(str)

    def __init__(self, parent):
        super().__init__(parent)
        self.r = sr.Recognizer()

    def run(self) :
        while True :
            print("reopen",datetime.datetime.now())

            with sr.Microphone() as source:
                print("open",datetime.datetime.now())
                audio = self.r.listen(source)

            # Speech recognition using Google Speech Recognition
            try:
                # for testing purposes, we're just using the default API key
                # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                # instead of `r.recognize_google(audio)`
                speachTyperResult = self.r.recognize_google(audio, language='ko-KR')
                self.typeSpeachResultSignal.emit(speachTyperResult)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))