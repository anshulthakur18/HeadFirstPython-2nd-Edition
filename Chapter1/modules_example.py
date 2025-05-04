'''
from os imprt getcwd  #importing the function
where_am_i = getcwd() #invoking the fucntion
'''

"""
Checking the system platform and version
import sys
sys.platform 
print("sys.verion")

# Getting the current working directory
import os 
os.getccwd()

#Changing the current working directory
os.chdir('/home/adam')

# Getting the environment variables
os.environ
os.getenv('HOME') # fetching one value out of all env. value

# Getting the current date and time
import datetime
datetime.date.today()
datetime.date.today().day
datetime.date.today().month
datetime.date.today().year
datetime.date.isoformat(datetime.date.today())

    strftime(...)
        strftime(format[, tuple]) -> string

        Convert a time tuple to a string according to a format specification.
        See the library reference manual for formatting codes. When the time tuple
        is not present, current time as returned by localtime() is used.

        Commonly used format codes:

        %Y  Year with century as a decimal number.
        %m  Month as a decimal number [01,12].
        %d  Day of the month as a decimal number [01,31].
        %H  Hour (24-hour clock) as a decimal number [00,23].
        %M  Minute as a decimal number [00,59].
        %S  Second as a decimal number [00,61].
        %z  Time zone offset from UTC.
        %a  Locale's abbreviated weekday name.
        %A  Locale's full weekday name.
        %b  Locale's abbreviated month name.
        %B  Locale's full month name.
        %c  Locale's appropriate date and time representation.
        %I  Hour (12-hour clock) as a decimal number [01,12].
        %p  Locale's equivalent of either AM or PM.
        
import time
time.strftime("%H:%M")
time.strftime("%A %p")
time.strftime('%d-%m-%Y %I:%M:%S %p')



if today == 'Saturday';
  print('PARTY!!!!')
elif today == 'Sunday';
  print('Recover')
else:
  print('Work, work, work')
"""