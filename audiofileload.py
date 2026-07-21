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
   y,sr=sf.read(path)
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



if __name__ == "__main__":

   file_path=r"C:\Users\USER\Desktop\pytorch_basics\test.wav"

   audio_data,sample_rate=load_librosa(path=file_path)
