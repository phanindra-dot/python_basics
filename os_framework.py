import os

def return_files_path(path):
  a=[]
  for root,dirs,files in os.walk(path):
    for i in files:
      a.append(os.path.join(path,i))
  return a

def return_files_names(path): # returns all files in a folder
  l=[]
  for i in os.listdir(path):
    l.append()
  return l

def return_base_name(path):
  e=os.path.basename(path)   # basename means the last name here stream_fp8_op_par
  return e

def return_all_wav_files(path): # return all the wav files names in all the folders in a given path including the wav in the path.
  l=[]
  for root,dirs,files in os.walk(path):
    for i in files:
      if i.endswith('.wav'):
        l.append(i)
  return l

def return_all_wav_files_paths(path): # return all the wav files path name in all the folders in a given path and also in the given path.
  a=[]
  for root,dirs,files in os.walk(path):
    for file in files:
      if file.endswith('.wav'):
        a.append(os.path.join(root,file))
  return a

def return_all_wav_files_except_inthat(path): # return all the wav files names in all the folders in a given path excluding the wav in the path.
  l=[]
  for root,dirs,files in os.walk(path):
    for i in files:
      if i.endswith('.wav'):
        if root is not path:
          l.append(i)
  return l


if __name__=="__main__":
  path=r"C:\Users\USER\Desktop\stream_fp8_op_par"
  b=return_all_wav_files_except_inthat(path)
  print(b)



   

