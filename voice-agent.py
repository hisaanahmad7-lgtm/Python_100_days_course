from gtts import gTTS

text = "Hy Hisaan Ahmad how are you! "

tts = gTTS(text=text, lang='en')
tts.save("MyIntro.mp3")
print("Audio File saved Successfully! ")