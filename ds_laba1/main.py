import pyodbc

if __name__ == '__main__':

    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=tcp:laba1sqlserver.database.windows.net,1433;'
        'DATABASE=Laba1DataBase;'
        'UID=azureuser;'
        'PWD=Azure134'


    )
    cursor = connection.cursor()
    cursor.execute("SELECT TOP 20 pc.Name as CategoryName, "
                   "p.name as ProductName FROM SalesLT.ProductCategory pc "
                   "JOIN SalesLT.Product p ON pc.productcategoryid = p.productcategoryid;")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    connection.close()
