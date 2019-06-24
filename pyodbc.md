<pre>
import pyodbc

connection= pyodbc.connect('DSN=OGE64;UserId=pihpj;Password=Okcoge2103t;')

connection.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')
connection.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
connection.setdecoding(pyodbc.SQL_WMETADATA, encoding='utf-8')
connection.setencoding(encoding='utf-8')

cursor= connection.cursor()
print ("Connected to Database!")

cursor.execute("Select 'Hello World' y")
t = cursor.fetchone()
print(t.y)
print("Bye")
</pre>
