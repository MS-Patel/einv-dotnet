import pyodbc


conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};" "Server=192.168.0.200,1433;" "uid=msp;" "pwd=msp@123;" "Database=invoice;" "Trusted_Connection=no;")

def read(conn):
    cursor = conn.cursor()
    cursor.execute("select * from invoice_details")

    for row in cursor:
        print(f'row = {row}')
        print()

read(conn)