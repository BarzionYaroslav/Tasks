import sqlite3
connect = sqlite3.connect('base.sqlite')
cursor = connect.cursor()
cursor.execute("SELECT Name FROM Customer JOIN Invoice ON Customer.CustomerId=Invoice.CustomerId JOIN InvoiceLine ON Invoice.InvoiceId=InvoiceLine.InvoiceId JOIN Track ON InvoiceLine.TrackId=Track.TrackId")
print(cursor.fetchall())