# Text to Speech Converter Project

from tkinter import *
from gtts import gTTS

import os

root = Tk()

frame1 = Frame(root,bg = "lightblue",height = "150")

frame1.pack(fill = X)

frame2 = Frame(root,bg = "lightgreen",height = "750")
frame2.pack(fill=X)

label = Label(frame1, text = "Write your Text here to convert it into Speech",font = "bold, 40",bg = "lightblue")

label.place(x = 200, y = 10)

entry = Entry(frame2, width = 60,bd = 6, font = 16)

entry.place(x = 400, y = 30)
entry.insert(0, "")

def play():

	language = "en"

	mytext = gTTS(text = entry.get(),lang = language,slow = False)

	mytext.save("output.mp3")

	os.system("start output.mp3")

btn = Button(frame2, text = "Done",width = "40", pady = 10,font = "bold, 16",command = play, bg='yellow')

btn.place(x = 440,y = 80)

# give a title
root.title("text_to_speech_convertor")


#change the size
root.geometry("650x550+350+200")

# start the gui
root.mainloop()





