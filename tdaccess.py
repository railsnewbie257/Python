import teradata

udaExec = teradata.UdaExec (appName="HelloWorld", version="1.0",
        logConsole=False)

session = udaExec.connect(method='odbc', system='TD1', authentication='LDAP',
        username='pihpj', password='Okcoge2103d');

for row in session.execute("select top 1 * from dl_oge_analytics.pih_fastload"):
    print(row)
    
