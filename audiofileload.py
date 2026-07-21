import librosa
import soundfile as sf
import torchaudio as ta
import torch
import numpy
import time 


def load_librosa(path):
   start = time.time()
   y,sr=librosa.load(path=path,sr=None)
   end = time.time()
   print(y.shape)
   print(sr)
   print(y)dea
   print(end-start)
   return y,sr



def load_sound_file(path):
   start=time.time()
   print(start)
   y,sr=sf.read(path)
   end=time.time()
   print(end)
   print(end-start)
   print(y.shape)
   print(sr)
   print(y)
   return y,sr

def load_torch_audio(path):
   y,sr=ta.load(path)
   print(y.shape)
   print(sr)
   print(y)
   return y,sr

def load_stft(x):
   X=torch.stft(x,n_fft=512,win_length=512,hop_length=256,return_complex=True)
   return X

if __name__ == "__main__":

   file_path=r"C:\Users\USER\Desktop\pytorch_basics\test.wav"

   audio_data,sample_rate=load_librosa(path=file_path)
   #audio_data = audio_data.squeeze(0)
   #print(type(audio_data))
   #print(audio_data.shape)
   #a=load_stft(audio_data)
   #print(a)
   #print(a.shape)

   torch.stft()