import numpy as np
import librosa
import matplotlib.pyplot as plt

def find_peaks(data, threshold=0.01):
    peaks = []
    in_peak = False
    peak_start = 0
    for i, value in enumerate(data):
        if value > threshold:
            if not in_peak:
                in_peak = True
                peak_start = i
        else:
            if in_peak:
                in_peak = False
                peak_end = i
                peaks.append((peak_start, peak_end))
    return peaks

def main():
    audio_file = "test.wav"
    y, sr = librosa.load(audio_file)

    y_abs = np.abs(y)
    
    window_length = 501  #window size = T * SR
    y_smooth = np.convolve(y_abs, np.ones(window_length)/window_length, mode='same')

    peaks = find_peaks(y_smooth)

    for i, (start, end) in enumerate(peaks):
        duration = (end - start) / sr
        print(f"Peak {i+1}: Duration = {duration:.2f} seconds")


if __name__ == "__main__":
    main()