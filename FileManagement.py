import sys, subprocess

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

