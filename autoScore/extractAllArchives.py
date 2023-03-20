import os
import shutil
from pathlib import Path

def extract_all_archives(root_dir):
    count =0 
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for file in filenames:
            if(file.endswith(".zip") or file.endswith(".rar") ):
                filepath = os.path.join(dirpath, file)
                # print(type(Path(file).suffix))
                fileTYPE = Path(file).suffix.strip(".")
                try:
                    shutil.unpack_archive(filepath, extract_dir=dirpath)
                    count+=1
                except:
                    print(f"Error extracting {filepath}")
    print(f"extracted {count} files")
root_dir = "../studentHws"
extract_all_archives(root_dir)