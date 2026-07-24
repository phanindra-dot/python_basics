# This script creates a BAT file for a single reference WAV file
# and multiple vector files found in a specified path (including all subdirectories).

import os
import pandas as pd
import argparse

def wav_filepath(path):
  wav_path_list=[]
  for root,dirs,files in os.walk(path):
    for file in files:
      if file.lower().endswith('.wav'):
        filepath=os.path.join(root,file)
        wav_path_list.append(filepath)
  return(wav_path_list)

def join_ref(file_list,ref_path):
  line=[]
  for filepath in file_list:
    line.append(f"{ref_path} , {filepath}")
  return line

def save_bat(ref_path,folder_path,bat_path,bat_name):
  if not os.path.isfile(ref_path):
    raise FileNotFoundError(f"Reference file is not found")
  if not os.path.isdir(folder_path):
    raise NotADirectoryError(f"Folder path is not found")
  os.makedirs(bat_path, exist_ok=True)
  filelist=wav_filepath(folder_path)
  b=join_ref(filelist,ref_path)
  file_name=os.path.join(bat_path,bat_name)
  df = pd.DataFrame(b)
  df.to_csv(file_name, sep=",", index=False, header=False)
  return len(filelist)
  

if __name__=="__main__":
  parser=argparse.ArgumentParser(
    description="Pass the required arguments"
  )
  parser.add_argument('-r','--ref_path',default=r"C:\Users\USER\Desktop\meeami_regular_16k\Clean_Speech_male_female.wav",
                      help="Add the ref filepath")
  parser.add_argument('-f','--folder_path',default=r"C:\Users\USER\Desktop\meeami_regular_16k",
                      help="add the folder_path conating wavs")
  parser.add_argument('-s','--bat_path',default=r"C:\Users\USER\Desktop\gru_to_conv",
                      help="add the folder_path where you want to save the bat file")
  parser.add_argument('-n','--filename',default="bat_file.bat",
                      help='add the filename how you want to save the bat file')

  args = parser.parse_args()
  l=save_bat(args.ref_path,args.folder_path,args.bat_path,args.filename)
  print(f"Number of files found in {args.folder_path} is {l}")
  print(f"Bat file is saved in {args.bat_path} with name {args.filename}")
  

