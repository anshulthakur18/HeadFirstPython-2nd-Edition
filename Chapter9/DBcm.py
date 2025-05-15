# Database context manager

import mysql.connector


class UseDatabase:
  def __init__(self, config:dict)-> None:       #Dunder init accepts a single dictionary argument
    self.configuration = config                 #The value of config is assigned to an attributr called "configuration"
    
  def __enter__(self)-> 'cursor':               #Annotation of this calss tell users that the method returns a cursor object
    self.conn   = mysql.connector.connect(**self.configuration) # Passing the dbconfig dictionary to the connect method of the mysql.connector module
    self.cursor = self.conn.cursor()            # The cursor method of the connection object is called to create a cursor object
    return self.cursor

#There’s a complication with dunder exit, which has to do with handling any exceptions that might occur within the with’s suite. 
# When something goes wrong, the interpreter always notifies __exit__ by passing three arguments into the method: exc_type, exc_value, and exc_trace.

  def __exit__(self, exc_type, exc_value, exc_trace)-> None:
    self.conn.commit()                        #The commit method of the connection object is called to save any changes made to the database
    self.cursor.close()                       #The close method of the cursor object is called to close the cursor
    self.conn.close()                         #The close method of the connection object is called to close the connection
    pass
