from django.shortcuts import render
import speech_recognition as sr
import pyaudio

# Create your views here.
def speechText(request):
    listener = sr.Recognizer()
    with sr.Microphone() as input_source:    #initialising microphone as input source
        voice_input = listener.listen(input_source)    #listening from microphone
        text = listener.recognize_google(voice_input)  #passing voice_input to recognizer and convert it into text
    
        return render(request,'deaf.html',{'message':text}) 
        
        