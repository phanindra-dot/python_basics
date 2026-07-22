# This script compares the list of WAV files in one folder with those in another folder.
# It returns the list of WAV files that are missing from the other folder.
import os

def return_filenames(path):
  filelist=[]
  for file in os.listdir(path):
      if file.endswith('.wav'):
        filelist.append(file)
  return filelist


def compare_lists(list1,list2):
  files_not_in_list2=[]
  for filename in list1:
     if filename not in list2:
        files_not_in_list2.append(filename)
  return files_not_in_list2

if __name__=="__main__":
    folder_1=r"C:\Users\USER\Desktop\meeami_regular_16k"
    folder_2=r"C:\Users\USER\Desktop\F4_P3_v2_outputs"
    list_1=return_filenames(folder_1)
    list_2=return_filenames(folder_2)
    result=compare_lists(list_1,list_2)
    print(f"These list of files are not found in {folder_2} : {result}")


            
            
          