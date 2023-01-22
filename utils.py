import os
import shutil
import re

#create numbered sub directories in a root folder
def create_sub_dirs(n,root,sub_dir_pfx, sub_dir_sfx = ""):
    for d in range(n):
        directory = sub_dir_pfx
        directory = sub_dir_pfx
        if len(str(d+1)) == 1 :
            str_d = '0'+str(d+1)
        else: str_d = str(d+1)
        directory += (f" {str_d} {sub_dir_sfx}")
        path = os.path.join(root, directory)
        try: 
            os.mkdir(path)
        except:
            pass

#return list of files (not directories) in a directory
def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

#put files into corresponding directory based on number in file name 
#Ex: DGD01 into DGD 1 folder
def sort_by_num(root, r_search, sub_dir_pfx, sub_dir_sfx = ""):
    for file in files(root):
        m = re.search(r_search, file)
        if m:
            d = m.groups()[0]
            #print(file)
            #print(d)
        
            directory = sub_dir_pfx
            if len(str(d)) == 1 :
                str_d = '0'+str(d)
            else: str_d = str(d)
            directory += (f" {str_d} {sub_dir_sfx}")


            current_path = os.path.join(root,file)
            new_path=os.path.join(root,directory,file)

            shutil.move(current_path, new_path)

#test r_search used in sort_by_num
def test_search(root, r_search):
    for file in files(root):
            m = re.search(r_search, file)
            if m:
                d = m.groups()[0]
                print(f"file: {file}  num: {d}")


#incomplete: some sort of universal directory name creator
def create_directory_name(sub_dir_pfx, sub_dir_sfx = "" ):
    for file in files(root):
            m = re.search(r_search, file)
            if m:
                d = m.groups()[0]
                print(f"file: {file}  num: {d}")
            
            directory = sub_dir_pfx
            if len(str(d)) == 1 :
                str_d = '0'+str(d)
            else: str_d = str(d)
            directory += (f" {str_d} {sub_dir_sfx}")
            print(directory)
