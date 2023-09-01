import sys, subprocess, re, os, shutil
from TreeItems.SplayTree import *

# this does work. I may want to manually change what application it uses. currently just uses the default
def open_file(path):
    try:
        if sys.platform.startswith('win'):
            print('Windows')
            subprocess.Popen(['start', path], shell=True)
        elif sys.platform.startswith('darwin'):
            print('Mac')
            subprocess.Popen(['open', path])
        elif sys.platform.starswith('linux'):
            print('Linux')
            subprocess.Popen(['xdg-open', path])
        else:
            return 'confused'
    except FileNotFoundError:
        print('unknown file')
    except Exception as e:
        print('Error ', str(e), ' occurred')

def fileDeterminer(string):
    # Match the string against a pattern that checks for the presence of an extension
    pattern = r".+\..+$"  # Matches strings with at least one character before a dot and at least one character after the dot
    match = re.match(pattern, string)
    
    if match:
        return "File"
    else:
        return "Folder"
    
def create_file(path, filename, splayTree):
    splayTree.insert(path + '/' + filename)
    open(path + '/' + filename, 'w').close()

def create_folder(path, foldername, splayTree):
    os.makedirs(path + '/' + foldername)

def delete_path(path, splayTree):
    if fileDeterminer(path) == 'File':
        os.remove(path)
        splayTree.delete(path)
    elif fileDeterminer(path) == 'Folder':
        file_list = os.listdir(path)
        ## MAY RESULT IN ISSUES
        for file in file_list:
            splayTree.delete(file)
        shutil.rmtree(path)
    else:
        raise RuntimeError("issue somewhere")

# used to obtain the "home" directory for the project
def home():
    home_dir = os.getcwd()
    home_dir += '/ManagedFiles'
    return home_dir