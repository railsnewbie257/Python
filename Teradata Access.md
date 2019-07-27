<pre>
conda install teradata

https://downloads.teradata.com/tools/reference/teradata-python-module
</pre>

[Connecting Python with Teradata using Teradata module](https://stackoverflow.com/questions/35938320/connecting-python-with-teradata-using-teradata-module)
[Python with Teradata ODBC](http://downloads.teradata.com/blog/odbcteam/2016/02/python-with-teradata-odbc)

<pre>
import teradata
  
udaExec = teradata.UdaExec (appName="HelloWorld", version="1.0", logConsole=False)

session = udaExec.connect(method="odbc", system="TD1", username=<b><em>username</em></b>, password=<b><em>password</em></b>, authentication="LDAP")
</pre>




