import sys
import pyodbc

#___________________________________________Dot Net Code_____________________________________________
import clr
from System.Reflection import Assembly
Assembly.LoadFile(r"D:\einv-dotnet\app\dll\System.Net.Http.Extensions.dll")
Assembly.LoadFile(r"D:\einv-dotnet\app\dll\System.Net.Http.Primitives.dll")
Assembly.LoadFile(r"D:\einv-dotnet\app\dll\System.Net.Http.Formatting.dll")
Assembly.LoadFile(r"D:\einv-dotnet\app\dll\BouncyCastle.Crypto.dll")
Assembly.LoadFile(r"D:\einv-dotnet\app\dll\Newtonsoft.Json.dll")

clr.AddReference("dll/Calc")
clr.AddReference("System.Net.Http.Extensions")
clr.AddReference("System.Net.Http.Primitives")
clr.AddReference("System.Net.Http.Formatting")
clr.AddReference("Newtonsoft.Json")




#___________________________________________Python Code_____________________________________________

conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};" "Server=DESKTOP-FV0B6MO\SQLEXPRESS;" "uid=msp;" "pwd=msp@123;" "Database=invoice;" "Trusted_Connection=no;")

def read(conn):
    cursor = conn.cursor()
    cursor.execute("select * from invoice_details")

    # for row in cursor:
    #     print(f'row = {row}')
    #     print()

read(conn)

#___________________________________________Dot Net Code_____________________________________________
from Calc import Program

obj  = Program()

api= obj.call_server_api()
print(api)
