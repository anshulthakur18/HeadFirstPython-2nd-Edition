Set the Password
```sql
-- To update the password for the MySQL user
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'your_new_password';
FLUSH PRIVILEGES;
```

```
-- To update the password 
ALTER USER 'vsearch'@'%' IDENTIFIED BY 'new_password';
FLUSH PRIVILEGES;
```

Select the Database:
```
USE vsearchlogDB
```

Get list of Users in MySQL

```
SELECT User, Host FROM mysql.user;
```

Creation of table:
```
create table log (
  id int auto_increment primary_key,
  ts timestamp default current_timestamp,
  phrase varchar(128) not null,
  letters varchar(32) not null,
  ip varchar(16) not null,
  browser_string varchar(256) not null,
  results varchar(64) not null);
```

```
---confirm the table created
describe log;
```

Information required for connecting to MySQL database: Host, UserID, password, name of the database.
```
--- MySQL connector 
dbconfig = { 'host': '127.0.0.1',
              'user': 'vsearch',
              'password': 'vsearchpasswd',
              'database': 'vsearhlogDB',
}
```
Import you database driver
```
import mysql.connector
```

Establish a connection to the server
```
conn = mysql.connector.connect(**dbconfig) 
--- The ** notation tells the connect function that a dictionary of arguments is being supplied in a single variable
```

Open a Cursor
```
--- Send SQL commands to the Database. Cursor as the database equivalent of the file handle

cursor = conn.cursor()
```

SQL queries

```
--- cursor variable lets you send the SQL queries to MySQL database
--- A triple-quoted string is used because SQL queries can often run to multiple lines, and using a triple-quoted string temporarily switches off the Python interpreter’s “end-of-line is the end-of-statement” rule.

_SQL = """show tables"""
cursor.execute(_SQL)
```
```
--- Above command will execute the queries but will not bring the results. We need to ask them
--- Using one of three cursor methods: 
        cursor.fetchone retrieves a single row of results.
        cursor.fetchmany retrieves the number of rows you specify. 
        cursor.fetchall retrieves all the rows that make up the results.
```

Fetching the result
```
res = cursor.fetchall()
res
```

Making code dynamic
```
---Python’s DB-API lets you position “data placeholders” in your query string, which are filled in with the actual values when you call cursor.execute. In effect, this lets you reuse a query with many different data values, passing the values as arguments to the query just before it’s executed. The placeholders in your query are stringed values, and are identified as %s in the code.

```

Database behaviour
```
For instance, if you use insert to send data to a table, then immediately use select to read it back, the data may not be available, as it is still in the database system’s cache waiting to be written. If this happens, you’re out of luck, as the select fails to return any data. Eventually, the data is written, so it’s not lost, but this default caching behavior may not be what you desire. If you are happy to take the performance hit associated with a database write, you can force your database system to commit all potentially cached data to your table using the conn.commit method. Let’s do that now to ensure the two insert statements from the previous page are applied to the log table. With your data written, you can now use a select query to confirm the data values are saved:
```

Writing to database immediately 
```
conn.commit()
_SQL="""select * from log"""
cursor.execute(_SQL)
for row in cursor.fetchall():
    print(row)
```

Close your cursor and connection
```
cursor.close()
conn.close()
```