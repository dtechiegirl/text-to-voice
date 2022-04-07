from gtts import gTTS
import os


mytext = input("what text do you want to convert to speech? ")
lang = input("english: en, French: fr, Mandarin: zh-Tw, Portuguese (Portugal): pt spanish:es")
myobj = gTTS(text=mytext, lang=lang,  slow=False)
myobj.save("voice.mp3")
os.system("voice.mp3")



