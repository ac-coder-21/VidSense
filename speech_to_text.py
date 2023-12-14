from pytube import YouTube
import subprocess
import torch
from huggingsound import SpeechRecognitionModel
import librosa
import soundfile as sf
import os

device = "cuda" if torch.cuda.is_available() else "cpu"
model = SpeechRecognitionModel("jonatasgrosman/wav2vec2-large-xlsr-53-english", device = device)

ffmpeg_command = [
    'ffmpeg',
    '-i', 'ytaudio.mp4',
    '-acodec', 'pcm_s16le',
    '-ar', '16000',
    'ytaudio.wav'
]

def speech_to_text(url):
    yt = YouTube(url)
    yt.streams.filter(only_audio = True, file_extension = 'mp4').first().download(filename = 'ytaudio.mp4')
    subprocess.run(ffmpeg_command)
    input_file = 'ytaudio.wav'
    stream = librosa.stream(input_file,block_length=30,frame_length=16000,hop_length=16000)

    for i,speech in enumerate(stream):
        sf.write(f'{i}.wav', speech, 16000)

    audio_path =[]
    for a in range(i+1):
        audio_path.append(f'{a}.wav')

    transcriptions = model.transcribe(audio_path)
    full_transcript = ' '

    for item in transcriptions:
        full_transcript += ''.join(item['transcription'])

    for d in audio_path:
        os.remove(d)
    os.remove('ytaudio.mp4')
    os.remove('ytaudio.wav')
    print(full_transcript)
    
    return full_transcript

