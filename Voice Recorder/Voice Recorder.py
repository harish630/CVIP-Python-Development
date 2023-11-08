'''Phase.2 - Task2'''
'''VOICE RECORDER'''

        
import sounddevice as sd
import soundfile as sf
from tkinter import *
  
  
def Voice_rec():
    fs = 48000
      
    duration = 5
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()
      
    
    return sf.write('my_Audio_file.flac', myrecording, fs)
  
  
master = Tk()
  
Label(master, text=" Voice Recoder : ").grid(row=0, sticky=W, rowspan=9)
  
  
b = Button(master, text="Start", command=Voice_rec)
b.grid(row=0, column=2, columnspan=5, rowspan=5,padx=9, pady=9)
  
mainloop()