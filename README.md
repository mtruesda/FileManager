# File Manager Using Splay Trees and Python

### Description of Project

I'm wriitng a file manager that uses a modified version of a splay tree to effectively allow a user to access files in a way that can be considered more efficient. It's intended to be modeled after the Windows file manager that also uses a splay tree.

I'm hoping that I can use the traversal functions to provide sections in my file manager such as a recents tab or a least recent tab. I'm also building additional features as I go.

I'm using Python because I have a lot of experiennce writing these sorts of projects in Python and I'm very comfortable with the modules that would be necessary to make something like this work well.

Something that had to be accounted for was the use of folders in my tree/directory. If something within the tree has a name without an extension, it is therefore a folder. This is determined through the use of a regex. The next step is to figure out how I'm going to add that to the path of the file.

## Description of Files

### Main.py

Runs the program using the other files available in the directory.

### tree.py

Uses a splay tree to handle the file manager. This will allow me to put together a recents selection and a bunch of other folders relating to different traversal methods.

As I go along, I have been finding random ways to improve my file manager. I've been considering adding balance to the tree
so that I can have an option to provide a more accurate recent and least recent section of my file manager. 

A big consideration when looking at what the keys of the nodes will look like is how to represent file locations. I'm currently planning to use filepaths.

### gui.py

This will be where the gui class is built. I'm considering building the class using tkinter and maybe making an attempt using another module like Kivy. The front end items will be contained here.

### FileManagement.py

this file just contains the backend code involved with determining the os and pulling up the file using the default application of the machine.

### pydot_graph_util.py

This is a visualizer that I repurposed from another project that actually turned out very useful. This is awesome.

### test.py

This is where most of my testing will be housed and a lot of tree models to use for those tests will be located.

## Using the File Manager

### Files Folder

The files folder will be where the files that come up in the file manager will be. 