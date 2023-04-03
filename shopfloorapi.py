import json
import pyodbc
import tkinter as tk
from flask import Flask
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
import data_connect
import requests
application = Flask(__name__)
application.app_context().push()
if(__name__=="__main__"):
    application.run()
#------------------------
connectionString = data_connect.GetConnectionString()
conn = pyodbc.connect(connectionString)
#------------------------
sqlstring = 'SELECT * FROM [PLCData].[dbo].[PLC_Master]'
cursor = conn.cursor()

@application.route('/')
def index():
    rootString = data_connect.GetRootString()
    return rootString

@application.route('/plcinfo/', methods=['GET'])
def get_plcinfo():
    sqlstring = 'SELECT * FROM [PLCData].[dbo].[PLC_Master]'
    plcinfo = []
    output = '{"PLC_Master":'
    cursor.execute(sqlstring)
    #create json return of plcinfo for each row in cursor
    for row in cursor:
        plcstring = 'Id: ' + str(row.id) + ', PLC_Address: ' + row.PLC_Address + ', PLC_Name: ' + row.PLC_Name
        plcinfo.append(plcstring)
        
    output += json.dumps(plcinfo)
    output += "}"
    return output

@application.route('/plcinfo/<plcid>', methods=['GET'])
def get_plcid(plcid):
    found = 0
    if plcid.isnumeric():
        sqlstring = 'SELECT * FROM [PLCData].[dbo].[PLC_Master] Where [id] = ' + plcid
        plcinfo = []
        output = '{"PLC_Master":'
        cursor.execute(sqlstring)
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