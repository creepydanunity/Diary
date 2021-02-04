import pyodbc
from datetime import datetime


class SQL:
    def __init__(self, database, server="CREEPYDAN\SQLEXPRESS"):
        self.conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                                   "Server="+server+";"
                                   "Database="+database+";"
                                   "Trusted_Connection=yes;")
        self.query = (datetime.now().strftime("%H:%M - %d/%m/%Y"))