# import write_audio
import Tkinter
#import Speech
#import wavtotext

global flagrec
flagrec = False
def rws():
    global flagrec
    flagrec = True
    if flagrec:
      #  write_audio.rec()
        print("RECORDING SAVED ")
        if flagrec:
            print ("Converting To Text")
            wavtotext.totext()
            flagrec = False

def rwos():
    global flagrec
    flagrec = True
    if flagrec:
        Speech.rec1()
        flagrec = False

GUI = Tkinter.Tk()
Canvas1 = Tkinter.Canvas(GUI, width=1000, height=1000)
Start = Tkinter.Button(GUI, text='Record with Saving', width=28, height=2, command=rws)
Start1 = Tkinter.Button(GUI, text='Record without Saving', width=28, height=2, command=rwos)

Exit = Tkinter.Button(GUI, text='Exit', width=28, height=2, command=exit)
Start1.pack()
Start.pack()
Exit.pack()
GUI.mainloop()
