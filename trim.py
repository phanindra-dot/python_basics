# This script trims all WAV files in a folder between the specified start and end times (in milliseconds).
import os
from pydub import AudioSegment
import argparse

def filepaths(path):
  if not os.path.isdir(path):
    raise NotADirectoryError("given folder_path not find")
  filelist=[]
  for root,dirs,files in os.walk(path):
    for file in files:
      if file.lower().endswith('.wav'):
        c=os.path.join(root,file)
        filelist.append(c)
  return filelist

def trimfile(filelist,trimed_path,start,end):
  os.makedirs(trimed_path,exist_ok=True)
  for file in filelist:
    audio=AudioSegment.from_file(file)
    trimmed_audio=audio[start:end]
    a=os.path.basename(file)
    c=os.path.join(trimed_path,a)
    trimmed_audio.export(c, format="wav")
  return len(filelist)

if __name__=="__main__":
  parser=argparse.ArgumentParser(description="This script helps to trim the audio file from 0 ms to x ms")
  parser.add_argument('-p','--path', default=r"C:\Users\USER\Desktop\meeami_regular_16k",
                      help="Add the folder path containing the files")
  parser.add_argument('-d','--save', default=r"C:\Users\USER\Desktop\gru_to_conv\trimmed",
                      help="Add the path of the folder where you want to save the files")
  parser.add_argument('-a','--start',default=0,
                      help="Add the start im ms where you want to start")
  parser.add_argument('-e','--end',default=1000,
                      help="Add the end im ms where you want to end")
  
  args=parser.parse_args()
  li=filepaths(args.path)
  a=trimfile(li,args.save,args.start,args.end)
  print(f"Total no fo files trimmed is :{a}")

