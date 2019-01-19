# txtFileManager.py module
# Module used to manipulate text files
# Coded by Lemur

from contextlib import contextmanager  # https://docs.python.org/2/library/contextlib.html
import os  # https://docs.python.org/2/library/os.html


def help():
    # Visual output of all the functions and brief description
    print('''
    ********* Python Text File Manager Package Functions... *********
    
    \ncreatefile(filename, [directory]) : function creates a file from two arguments,
    both strings, the file name and the directory. Do not specify directory if
    you want to write file into current one. Add '..' at start of path if you
    would like to go up a directory. A custom error message will be outputted if 
    your file path was not found
    
    \ndeletefile(filename, [directory]) : function deletes file if found. Otherwise,
    a custom error message is outputted. Add '..' at start of path if you would like to
    go up a directory, or leave it blank if want to work in current
    
    \nencryptfile(filename, [directory]) : function which encrypts a text file based on
    _________ algorithm
    
    \ndecryptfile(filename, directory, key) : function which decrypts a text file based on
    __________ algorithm
    
    \nwriteline(filename, [directory, text, line_number]) : function which writes a line of text 
    into the file in the specified directory. Line_number will be an integer representing the index
    of the line we will like to modify, but will be taken as 0 if file is empty. Custom error
    outputted if IndexError raised
    
    \nappendline(filename, [directory, text]) : function which appends a line to a file in
    specified directory. Similar functionality to 'writeline'
    
    \nfindline(filename, [directory, text]) : function that returns all of the line numbers where
    the specified line of text was found in the file.
    
    \ndeleteline(filename, [directory, line_number]) : function which deletes a specified line number
    in the file.
    
    \nfindfile(filename) : function which searches for a specified file in the cwd and returns its 
    full path if it is found (as a string).
    
    \nreadline(filename, [directory, line_number]) :
    
    \n**********************************************************
    ''')


@contextmanager
def createfile(filename, directory=""):
    '''
        Function's purpose is to create a file in a specified directory,
    overwriting the file if it already exists

    :param filename: string representing the name of the file to be created
    :param directory: string representing the directory in which file to be created
    '''

    # Check to see if user requests to go back
    directory = climb_directory(directory)

    # Change directory
    origdirectory = os.getcwd()
    try:
        # If no directory specified, just write it into current
        if directory != "":
            os.chdir(os.path.expanduser(directory))
        with open(filename, "w") as f:
            f.close()
    except OSError or WindowsError:
        print("\nSorry, your directory does not exist, try again")
    finally:
        os.chdir(origdirectory)
        print("\nFinished")


@contextmanager
def deletefile(filename, directory=""):
    '''
        Function which purpose is to find a file in a specified directory and delete
    it. If the file is not found, a custom error message is outputted

    :param filename: string representing the name of the file to be deleted
    :param directory: string representing the name of the directory in which the file is stored
    '''
    # Check to see if user requests to go back
    directory = climb_directory(directory)

    # Change directory
    origdirectory = os.getcwd()
    try:
        # If no directory specified, just take current one
        if directory != "":
            os.chdir(os.path.expanduser(directory))
        os.remove(filename)
    except OSError or WindowsError:
        print("\nSorry, your path was not found, or your file didn't exist")
    finally:
        os.chdir(origdirectory)
        print("\nFinished")


def climb_directory(directory):
    if directory[:2] == "..":
        climbs = len(directory)
        string_parameter = "." * climbs
        if directory[:climbs] == string_parameter:
            for jumps in range(climbs - 1):
                os.chdir("..")
                directory = directory[2:]
            return directory
    else:
        pass

def encryptfile():
    # FILE LEGNTH LINE
    # LOOP FOR EACH LINE
    # ENCRYPT LINE
    # REWRITE IN TEMP FILE
    # CHANGE NAME OF OLD FILE TO NEW FILE
    pass


def decryptfile():
    pass


@contextmanager
def writeline(filename, directory="", text="", line_number=0):
    '''
        Function which purpose is to write a line of text into a file in a specific
    directory. The line number will be specified by the user too, although it will be taken as
    0 if the file is originally empty, or will trigger a custom error if it is not found in the file

    :param filename: string representing the name of the file to be edited
    :param directory: string representing the name of the directory in which the file is found
    :param text: string representing the new line of text to be written into file
    :param line_number: integer representing line number to be edited within the file
    '''
    # Check to see if user requests to go back
    directory = climb_directory(directory)

    # Change directory
    origdirectory = os.getcwd()
    try:
        # If directory is not specified, take current one
        if directory != "":
            os.chdir(os.path.expanduser(directory))
        with open(filename, "r") as f:
            # Extract data from the file and store in a 1D Array
            data = f.readlines()
            f.close()

        # Change specified line in data (add newline at the end)
        if len(data) > 0:
            data[line_number-1] = text + '\n'
        else:
            # If no lines in file, just append the new one
            data.append(text + '\n')

        # Write new contents to the file
        with open(filename, "w") as f:
            f.writelines(data)
            f.close()
    except OSError or WindowsError:
        print("\nPath or file does not exist")
    except IndexError:
        print("\nThe line you specified does not exist in the file")
    finally:
        os.chdir(origdirectory)
        print("\nFinished")


@contextmanager
def appendline(filename, directory="", text=""):
    '''
        Function which purpose is to add a line of text, specified by the user, to the
    end of a file in a specified directory.
    :param filename: string representing the name of the file to be edited
    :param directory: string representing the name of the directory in which file is stored
    :param text: string representing the new line of text to be added
    '''
    # Check to see if user requests to go back
    directory = climb_directory(directory)

    # Change directory
    origdirectory = os.getcwd()
    try:
        # If directory is not specified, take current one
        if directory != "":
            os.chdir(os.path.expanduser(directory))
        with open(filename, "r") as f:
            # Read all lines in file and store them in a 1D Array
            data = f.readlines()
            f.close()

        # Append new line of text to the end
        data.append(text + '\n')

        with open(filename, "w") as f:
            # Write all data back in
            f.writelines(data)
            f.close()

    except OSError or WindowsError:
        print("\nPath or file not found")
    finally:
        os.chdir(origdirectory)
        print("\nFinished")


@contextmanager
def findline(filename, directory="", text=""):
    '''
        File which purpose is to search for a line specified by the user in a file stored
    in a certain directory. If the line is found, position where it was found is stored.
    The function returns a 1D array with all of the positions in which the line was found,
    as well as providing a visual output.

    :param filename: string representing the name of the file to be edited
    :param directory: string representing the name of the directory in which file is stored
    :param text: string representing the new line of text to be searched for
    :return: 1D array with all of the line numbers that matched with the query, or
    custom error message if path/file not found
    '''

    line = None

    # Check to see if user requests to go back
    # ¿Any more efficient way you guys can think of doing this?
    directory = climb_directory(directory)

    # Change directory
    origdirectory = os.getcwd()
    try:
        # If directory is not specified, take current one
        if directory != "":
            os.chdir(os.path.expanduser(directory))
        with open(filename, "r") as f:
            # Read all lines and store in a 1D Array
            data = f.readlines()
            f.close()

        # Search for specific line of text
        line = [i+1 for i in range(len(data)) if data[i] == text + '\n']

    except OSError or WindowsError:
        print("\nPath or file not found")
    finally:
        os.chdir(origdirectory)
        print("\nFinished")

    # Output results
    print("\nYour line of text was found in the following line/s: {}".format(line))
    return line


@contextmanager
def deleteline(filename, directory="", line_number=1):
    '''
        Function which purpose is to delete a specified line in a text file stored
    in a particular directory, based on the line_number entered by the user.
    :param filename: string representing the name of the file to be edited
    :param directory: string representing the name of the directory in which it is stored
    :param line_number: integer representing the line number to be deleted
    '''

    # Check to see if user requests to go back
    # ¿Any more efficient way you guys can think of doing this?
    directory = climb_directory(directory)

    # Change directory
    origdirectory = os.getcwd()
    try:
        # If directory is not specified, take current one
        if directory != "":
            os.chdir(os.path.expanduser(directory))

        with open(filename, "r") as f:
            # Store all of the lines in a 1D array
            data = f.readlines()
            f.close()

        # Delete specified line
        del data[line_number-1]

        with open(filename, "w") as f:
            # Re-write all modified data
            f.writelines(data)
            f.close()

    except OSError or WindowsError:
        print("\nPath of file not found")
    except IndexError:
        print("\nLine does not exist")
    finally:
        os.chdir(origdirectory)
        print("\nFinished")


def findfile(filename):
    '''
        Function which purpose is to search for a file in the cwd and return its
    full path.
    :param filename: string representing the name of the file to be found
    :return: full path (string) of the file searched for
    '''
    for root, dirs, files in os.walk(os.getcwd()):
        if filename in files:
            return os.path.join(root, filename)

help()

@contextmanager
def readline(filename, directory="", text=0):
    pass
