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
            return 'unsupported platform...?'
    except FileNotFoundError:
        print('File not found')
    except Exception as e:
        print('Error ', str(e), ' occurred')

# my attempt to tie regex into this project
def fileDeterminer(string):
    pattern = r".+\..+$"              # Match the string against a pattern that checks for the presence of an extension
    match = re.match(pattern, string) # Matches strings with at least one character before a dot and at least one character after the dot
    return "File" if match else "Folder"

# creates the file and then inserts it into the Splay Tree. For whatever reason it's not doing that though.
def create_file(path, filename, splayTree):
    full_path = os.path.join(path, filename)
    try:
        with open(full_path, 'w') as f:
            pass  # File is created and immediately closed
        splayTree.insert(full_path)
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")

# self-explanatory
def create_folder(path, foldername, splayTree):
    os.makedirs(path + '/' + foldername)

# determines if what I'm deleting is a folder or file and deletes accordingly
def delete_path(path, splayTree):
    try:
        if fileDeterminer(path) == 'File':
            os.remove(path)
            splayTree.delete(path)
        else:
            shutil.rmtree(path)
            for root, dirs, files in os.walk(path):
                for name in files:
                    splayTree.delete(os.path.join(root, name))
    except Exception as e:
        print(f"An error occurred while deleting: {e}")

# used to obtain the "home" directory for the project
def home():
    return os.path.join(os.getcwd(), 'ManagedFiles')