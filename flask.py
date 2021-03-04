import os
# import zipfile
# import uuid

from flask import Flask, flash, request, redirect, url_for, send_from_directory

from spleeter.separator import Separator
from spleeter.audio.adapter import AudioAdapter

app = Flask(__name__)
if __name__ == '__main__':

    separator = Separator('spleeter:5stems')

    audio_loader = AudioAdapter.default()
    sample_rate = 44100
    waveform, _ = audio_loader.load("audio/Never Catch Me.mp3", sample_rate=sample_rate)

    prediction = separator.separate(waveform, audio_descriptor='')
    print(prediction)

    for instrument, data in prediction.items():
        audio_loader.save(os.path.join("output", f'{instrument}.mp3'), data, sample_rate, 'mp3', '128k')

# ALLOWED_EXTENSIONS = ['mp3', 'wav']



# virtualenv E:\Code\spleeter-back-end\venv -p C:/Users/aidan/AppData/Local/Programs/Python/Python38/python.exe
# virtualenv --python=E:\Code\spleeter-back-end\venv C:/Users/aidan/AppData/Local/Programs/Python/Python38/python.exe

# .\venv\Scripts\activate