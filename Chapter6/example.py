# Python Supports Open, Process, Close

todos = open('todos.txt', 'a')              # Open the file in append mode
print('Put out the trash.', file=todos)     # Write to the file and print takes extra argument file stream
print('Feed the cat.', file=todos)
print('Prepare tax return.', file=todos)
todos.close()                               # Close the file 

#Opening the file assigns a file object to the variable
tasks = open('todos.txt')                   # Open the file in read mode
for chore in tasks:                          # Iterate through the file
    print(chore, end='')                     # Print each line without extra newline
tasks.close()                               # Close the file

#A Better Open, Process, Close: “with”
with open('todos.txt') as tasks:            # Open the file and assign file stream to tasks 
    for chore in tasks:                     # Iterate through the file 
        print(chore, end='')                # Print each line without extra newline
#The with statement is smart enough to remember to call close on your behalf whenever its suite of code ends.

with open('todos.txt', 'o') as log:
    contents = log.read()                  # Read the contents of the file
    print(contents)                        # Return the contents of the file

#However, the interpreter provides a read method, which, when invoked, returns the entire contents of the file “in one go.”