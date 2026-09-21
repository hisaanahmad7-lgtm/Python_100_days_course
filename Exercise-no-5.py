# from gtts import gTTS
# from io import BytesIO
# import pygame

# text = "Kindly Drink Water"

# # Generate speech in memory (no file saved)
# mp3_fp = BytesIO()
# tts = gTTS(text=text, lang='en')
# tts.write_to_fp(mp3_fp)
# mp3_fp.seek(0)

# # Play directly from memory
# pygame.mixer.init()
# pygame.mixer.music.load(mp3_fp)
# pygame.mixer.music.play()

# while pygame.mixer.music.get_busy():
#     pygame.time.Clock().tick(10)


import pyautogui as pag
import time 
# from gtts import gTTS
# mytext = "Please Drink water"
while True:
    # tts = gTTS(text=mytext, lang='en')
    # tts = gTTS(text=mytext, lang='en')
    # tts.save("welcome.mp3")
    pag.alert(text="Hisaan Ahmad Drink Water ", title="alert title")
    time.sleep(5)


#     tts = gTTS(text=mytext, lang='en')
# tts.save("welcome.mp3")