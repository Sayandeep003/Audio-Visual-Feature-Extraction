import wave
import numpy as np
import sys
import matplotlib.pyplot as plt
from matplotlib import style
wav=wave.open("Audio File of Video 2 mono.wav","r")
raw= wav.readframes(-1)
raw=np.frombuffer(raw,dtype='int16')
SampleRate=wav.getframerate()
Time= np.linspace(0, len(raw)/SampleRate, num= len(raw))
plt.title("Graphical Representation of the Audio File")    
plt.plot(Time,raw, color="blue") 
plt.ylabel("Amplitude")       
plt.xlabel("Time in sec")
style.use('ggplot')
plt.show()

