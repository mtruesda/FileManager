# File Manager Using Splay Trees and Python

### Description of Project

I'm writing a file manager that uses a lightly modified version of a splay tree to effectively allow a user to access files in a way that can be considered more efficient. It's intended to be modeled after the Windows file manager that also uses a splay tree.

I'm hoping that I can use the traversal functions to provide sections in my file manager such as a recents tab and other important orders that I may want. I'm also building additional features as I go.

I'm using Python because I have a lot of experiennce writing these sorts of projects in Python and I'm very comfortable with the modules that would be necessary to make something like this work well.

The folders shouldn't impact the tree itself too much. They will be accounted for when it's necessary such as when deleting or inserting files. The hard part will be accounting for filepaths when opening and accessing files. Something I haven't accounted for though (yet), is movement of files or folders.

Something that recently came to mind was adjusting the paths entered into the tree so that it doesn't matter what computer you're working from. The way the tree is currently set up, the paths are all completely based on the machine on which you run the program.

## Description of Files

### Main.py

Runs the program using the other files available in the directory. This file makes use of Tkinter to put together the gui that represents the file manager along with some of the necessary functions.

### SplayTree.py

Uses a splay tree to handle the file manager. This will allow me to put together a recents selection and a bunch of other folders relating to different traversal methods.

As I go along, I have been finding random ways to improve my file manager. I've decided to take a BST approach with insertion because it results in something that allows the user to get a better and more accurate representation of a recents section when doing traversal.

A big consideration when looking at what the keys of the nodes will look like is how to represent file locations. I'm currently planning to use filepaths. I haven't quite found any other way of doing it.

### FileManagement.py

this file just contains the backend code involved with determining the os and pulling up the file using the default application of the machine.

This is also where the functions used to modify the actual storage and tree are located.

### pydot_graph_util.py

This is a visualizer that I repurposed from another a school project that actually turned out very useful. This is awesome.

### Tests.py

This is where most of my testing will be housed and a lot of tree models to use for those tests will be located. My tests don't entirely resemble unit tests as I largely make use of the visualizer for my testing. There are a few unit tests at the end, however.

## Using the File Manager

### ManagedFiles Folder

This folder will be where the files that come up in the file manager will be.