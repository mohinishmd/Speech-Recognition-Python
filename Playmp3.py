import pymedia
import time
import Tkinter

message = 'G:\Songs\Music\Heroes.mp3'
player = pymedia.Player()


def PlayM():
    player.start()
    print("Playing:")
    player.startPlayback(message)

def PlayM1(message1):
    player.startPlayback(message1)


while player.isPlaying():
    time.sleep(0.01)


def ResumeM():
    player.unpausePlayback()


def PauseM():
    player.pausePlayback()


def NextM():
    #player.stopPlayback()
    message = 'G:\Songs\Music\Blank Space.mp3'
    PlayM1(message)
    #player.startPlayback(message)


def PreviousM():
    message = 'G:\Songs\Music\Heroes.mp3'
    player.startPlayback(message)


GUI = Tkinter.Tk()
Canvas1 = Tkinter.Canvas(GUI, width=1000, height=1000)
Start = Tkinter.Button(GUI, text='Start The Song', width=18, height=2, command=PlayM)
Resume = Tkinter.Button(GUI, text='Resume The Song', width=18, height=2, command=ResumeM)
Pause = Tkinter.Button(GUI, text='Pause The Song', width=18, height=2, command=PauseM)
Next = Tkinter.Button(GUI, text='Next', width=18, height=2, command=NextM)
Previous = Tkinter.Button(GUI, text='Previous', width=18, height=2, command=PreviousM)
Start.pack()
Resume.pack()
Pause.pack()
Next.pack()
Previous.pack()
GUI.mainloop()
