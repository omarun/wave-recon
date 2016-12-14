# The program demonstrates an environment to perform an analysis of the frequencies of a two-channel wave audio source.  For this step, 
# DTFT (Discrete Time Fourier Transform) of the wave audio source (a wave file) is performed.
# Assuming that the necessary analysis is performed, next step is to "sew back" the original wave audio from the frequency information.  
# For this, the IDTFT (Inverse Discrete Time Fourier Transform)is used.  To play the reconstructed wave audio, the contents are written
# into a output wave file "Output.wav". Playback of this file is attempted to verify the authenticity of the reconstructed data.

# Importing the essential sound and plot modules 
import winsound
import wave
import matplotlib.pyplot as plt
import numpy as np

# Importing the essential FFT/DTFT and IFFT/IDTFT modules
from scipy.fftpack import fft, ifft
from scipy.io import wavfile # get the api

# Defining the source and destination files.  These should be present in the same folder as of this script file.
source = r".\input file.wav"
destination = r".\output file.wav"

# Play the source audio file for the listener
winsound.PlaySound(source, winsound.SND_FILENAME)

# Step 1: Perform DTFT of the source audio
fs, data = wavfile.read(source) # load the data
data = data.T[0] # This is to extract information from the first channel of the two channel soundtrack

# Plot the audio data in a chart.  This is how the audio "looks" like in the time domain.
plt.figure(1)
plt.plot(data,'r') 
plt.title("Time Domain of Input Audio. Closing these windows will start Step 2.")
plt.xlabel("time")
plt.ylabel("amplitude")

fftdata = fft(data) # calculate fourier transform (complex numbers list)
xval = np.linspace(0.,fs,(len(fftdata)-1))

# Plot the frequency data, which is the output of the DTFT
plt.figure(2)
plt.plot(xval, abs(fftdata[:(len(fftdata)-1)]),'r') 
plt.title("Frequency Spectrum of Input Audio.  Closing these windows will start Step 2.")
plt.xlabel("frequency samples")
plt.ylabel("amplitude")
plt.show()

# Step 2: Perform IDTFT of the frequency data
ifftdata = ifft(fftdata)
ifftdataround = np.round(ifftdata).astype('int16')

# Write the reconstructed results into the output wave file.
wavfile.write(destination,fs,ifftdataround)

# Play the wave file
winsound.PlaySound(destination, winsound.SND_FILENAME)

# Plot the timeline of the reconstructed wave audio.
plt.figure(3)
plt.plot(ifftdata.real, 'g')
plt.title("Time domain of Reconstructed Audio")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.show()

# End of program.  Designed and implemented by Varun Chandramohan, 2016.