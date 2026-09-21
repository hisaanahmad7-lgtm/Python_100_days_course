

from gtts import gTTS
text =" Twinkle, twinkle, little star, how I wonder what you are, up above the world so high, like a diamond in the sky, when the blazing sun is gone, when he nothing shines upon, then you show your little light, twinkle, twinkle, all the night, then the traveller in the dark thanks you for your tiny spark, he could not see which way to go, if you did not twinkle so, in the dark blue sky you keep, and often through my curtains peep, for you never shut your eye, till the sun is in the sky, as your bright and tiny spark lights the traveller in the dark, though I know not what you are, twinkle, twinkle, little star."
tts = gTTS(text=text, lang='en')
tts.save("welcome.mp3")


import pyttsx3

# text = "Hello Hisaan! Ye bina save kiye direct text read kar raha hai."

# engine = pyttsx3.init()
# engine.say(text)
# engine.runAndWait()
