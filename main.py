# Importing the numpy and matplotlib libraries.
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("darkgrid")

'''
Creates three sinusoidal signals with different frequencies and amplitudes, 
adds them together to create a composite signal, and stores it in z.
'''
# Creating a vector of 150 evenly spaced numbers between 0 and 1.
t = np.linspace(0, 1, 150, endpoint=False)
# Creating a sinusoidal signal with a frequency of 10 Hz.
x = np.sin(2*np.pi*10*t)
# Creating a sinusoidal signal with a frequency of 20 Hz.
y = 0.5*np.sin(2*np.pi*20*t)
# Creating a sinusoidal signal with a frequency of 50 Hz.
w = 0.2*np.sin(2*np.pi*50*t)
# Adding the three signals together.
z = x + y + w


# Taking the Fourier transform of the signal z.
zf = np.fft.fft(z)

'''
This is creating a vector of frequencies that correspond to the Fourier transform of the signal
'''
# Finding the length of the signal z.
N = len(z)
# Creating a vector of frequencies that correspond to the Fourier transform of the signal.
freq = np.fft.fftfreq(N, d=t[1]-t[0])
# Taking the absolute value of the Fourier transform of the signal and then dividing it by the length
# of the signal.
spectrum = 2/N * np.abs(zf[:N//2])


'''
Creating a mask that is false for frequencies between 15 and 60 Hz
'''
# Creating a vector of ones with the same length as the vector freq.
mask = np.ones(len(freq), dtype=bool)
# Creating a mask that is false for frequencies between 15 and 60 Hz.
mask[(freq > 15) & (freq < 60)] = False
# Creating a mask that is false for frequencies between 15 and 60 Hz.
mask[(freq < -15) & (freq > -60)] = False

'''
Creating a copy of the vector zf and then setting the values of the vector zf_filtered to zero for
the frequencies that are not allowed to pass
'''
# Creating a copy of the vector zf.
zf_filtered = zf.copy()
# Setting the values of the vector zf_filtered to zero for the frequencies that are not allowed to
# pass.
zf_filtered[~mask] = 0

# Taking the inverse Fourier transform of the filtered signal.
z_filtered = np.fft.ifft(zf_filtered)

plt.figure(figsize=(10,6))
plt.subplot(211)
plt.plot(t, x, label='X signal', color='red')
plt.plot(t, y, label='Y signal', color='blue')
plt.plot(t, w, label='W signal', color='orange')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Plot of the signals X, Y, and W')
plt.legend()
plt.subplot(212)
plt.plot(t, z.real, label='z signal', color='green')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Plot of the signal Z - Sum of X, Y, and W')
plt.legend()
plt.tight_layout()
plt.subplot(212)


# This is plotting the Fourier transform of the signal z.
fig3 = plt.figure()
plt.plot(freq[:N//2], spectrum)
plt.xlabel('Frequency [Hz]')
plt.ylabel('Amplitude')
plt.title('Plot 3')
plt.legend()

# This is plotting the Fourier transform of the signal z_filtered.
plt.figure(figsize=(10,6))
plt.subplot(211)
plt.plot(t, z, color='green')
plt.title('Original signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.subplot(212)
plt.plot(t, np.real(z_filtered), color='red')
plt.title('Filtered signal (only X signal allowed to pass)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()
