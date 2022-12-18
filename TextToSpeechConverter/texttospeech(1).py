# Text to Speech Converter Project

# Import the required module for text to speech conversion
from gtts import gTTS

# This module is imported so that we can  play the converted audio
import os

# The text that you want to convert in audio
mytext = " Hello everyone my name is Aryansh Singh this is my Python project of Text to Speech Converter:"

# Language in which you want to convert
language = 'en'

# Here we have marked slow=False. Which tells the module that the converted audio should  have a high speed
output = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named output
output.save("output.mp3")

# Playing the converted file
os.system("start output.mp3")

