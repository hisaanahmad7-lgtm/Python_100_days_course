from gtts import gTTS
text = "Hello, welcome to the Python course i hope that you will like this course and will make conscious efforts to learn python!"
tts = gTTS(text=text, lang='en')
tts.save("welcome.mp3")


import pyttsx3

# text = "Hello Hisaan! Ye bina save kiye direct text read kar raha hai."

# engine = pyttsx3.init()
# engine.say(text)
# engine.runAndWait()
