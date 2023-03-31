import json
import pyodbc
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import data_connect
import requests
appllication = Flask(__name__)
appllication.app_context().push()
if(__name__=="__main__"):
    appllication.run()
#------------------------
connectionString = data_connect.GetConnectionString()
conn = pyodbc.connect(connectionString)
#------------------------
sqlstring = 'SELECT * FROM [PLCData].[dbo].[PLC_Master]'
cursor = conn.cursor()
@appllication.route('/')
def index():
    rootString = data_connect.GetRootString()
    return rootString
@appllication.route('/plcinfo/', methods=['GET'])
def get_plcinfo():
    sqlstring = 'SELECT * FROM [PLCData].[dbo].[PLC_Master]'
    plcinfo = []
    output = '{"PLC_Master":'
    cursor.execute(sqlstring)
    for row in cursor:
        plcstring = 'Id: ' + str(row.id) + ', PLC_Address: ' + row.PLC_Address + ', PLC_Name: ' + row.PLC_Name
        plcinfo.append(plcstring)
    
    output += json.dumps(plcinfo)
    output += "}"
    return output
@appllication.route('/plcinfo/<plcid>', methods=['GET'])
def get_plcid(plcid):
    sqlstring = 'SELECT * FROM [PLCData].[dbo].[PLC_Master] Where [id] = ' + plcid
    plcinfo = []
    output = '{"PLC_Master":'
    cursor.execute(sqlstring)
    found = 0
    for row in cursor:
        found = 1
        plcstring = 'Id: ' + str(row.id) + ', PLC_Address: ' + row.PLC_Address + ', PLC_Name: ' + row.PLC_Name
        plcinfo.append(plcstring)

    if found == 1:
        output += json.dumps(plcinfo)
        output += "}"
        return output
    else:
        output = "There was no information found for ID " + plcid
        return output