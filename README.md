# txtfilemanager
“.txt file manager” python package

The purpose of this packages it to allow the easy manipulation of text files and to ensure security and integrity of it.


Functions within “.txt file manager”

• help()
Description: The help functions prints out all the functions available within the package. Together with a brief description of it and the parameters needed to call each function.


• createfile(filename, directory)
Description: Creates a file with the given name and in the directory specified.  It will overwrite any existent file with the same name in the same directory.


• deletefile(filename, directory)
Description: Deletes a file with the give name and in the directory specified. It will prompt an error if there is no such file.


• encryptfile(filename, directory)
Description: It encrypts the given file so it is illegible when opened with a text editor. It will also store the key within the text file so it can be decrypted. If a file is already encrypted it will prompt a suitable message.


• decryptfile(filename, directory, key)
Description: It decrypts the given file.


• writeline(filename, directory, text, line_number)
Description: Writes a new line in the given line number of the text file specified.


• appendine(filename, directory, text)
Description: Writes at the end of the file a new line of the text file specified.


• findline(filename, directory, text)
Description: It will try to find within the text file the lines that contain the given argument of text. Returning the lines in which it was found.

• deleteline(filename, directory, line_number)
Description: It will delete the line in the given line number of the text file specified.


• findfile(filename)
Description: It will try to find the specified file in memory. Returning it’s directory.
