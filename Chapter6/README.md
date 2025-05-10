“Reading” is the “open” function’s default mode.

A number of different values, and dictates the mode the file is opened in. Modes include “reading,” “writing,” and “appending.” Here are the most common mode values, where each (except for 'r') creates a new empty file if the file named in the first argument doesn’t already exist:
    'r' Open a file for reading. This is the default mode and, as such, is optional. When no second argument is provided, 'r' is assumed. It is also assumed that the file being read from already exists.
    'w' Open a file for writing. If the file already contains data, empty the file of its data before continuing.
    'a' Open a file for appending. Preserve the file’s contents, adding any new data to the end of the file (compare this behavior to 'w').
    'x' Open a new file for writing. Fail if the file already exists (compare this behavior to 'w' and to 'a').
By default, files open in text mode, where the file is assumed to contain lines of textual data (e.g., ASCII or UTF-8). If you are working with nontextual data (e.g., an image file or an MP3), you can specify binary mode by adding “b” to any of the modes (e.g., 'wb' means “write to a binary data”). If you include “+“ as part of the second argument, the file is opened for reading and writing (e.g., 'x+b' means “read from and write to a new binary file”).

The with statement is smart enough to remember to call close on your behalf whenever its suite of code ends.
