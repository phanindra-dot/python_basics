# This script writes the paths, sample rates, and lengths of all WAV files
# (including those in subdirectories) to a CSV file.
import os
import pandas as pd
import argparse
import soundfile as sf


def filepaths(path):
  filelist=[]
  for root,dirs,files in os.walk(path):
    for file in files:
      if file.lower().endswith('.wav'):
        c=os.path.join(root,file)
        filelist.append(c)
  return filelist
def sample_rate(filelist):
  sr_list=[]
  len_list=[]
  for file in filelist:
    y,sr=sf.read(file)
    b=len(y)/sr
    sr_list.append(sr)
    len_list.append(b)
  return sr_list ,len_list

def process(folder_path,csv_path,csv_name):
  if not os.path.isdir(folder_path):
    raise NotADirectoryError("folder_path given doesnot exist")
  os.makedirs(csv_path,exist_ok=True)
  files=filepaths(folder_path)
  a,b=sample_rate(files)
  file_name=os.path.join(csv_path,csv_name)
  d = {"col1": files, "col2": a, "col3": b }
  df=pd.DataFrame(d)
  df.to_csv(file_name,sep=",",header=["Filepath","SampleRate","Length(sec)"],index=False)
  return len(files)


if __name__=="__main__":
  parser=argparse.ArgumentParser(
        description="Give the required arguments properly")
  parser.add_argument('-p','--folder_path',default=r"C:\Users\USER\Desktop\meeami_regular_16k",
                      help='add the path of the folder which you want wav files')
  parser.add_argument('-s','--csv_path',default=r"C:\Users\USER\Desktop\gru_to_conv",
                      help="add the path where you want to save the csv")
  parser.add_argument('-n','--csv_name',default="phani.csv",
                      help="add the name of the csv file")
        
  args = parser.parse_args()

  a=process(args.folder_path,args.csv_path,args.csv_name)
  print(f"Filepaths are written to {args.csv_path} with {args.csv_name}")
  print(f"Number of files found in {args.folder_path} is {a}")



