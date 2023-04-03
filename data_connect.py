
def GetConnectionString():
    connectionString = 'DRIVER={SQL Server};SERVER=192.168.0.84;PORT=1433;DATABASE=PLCData;UID=nbty;PWD=nbty;'
    return connectionString

def GetRootString():
    # Create a menu of options explaining what the user can do with this web service.
    rootString = '<h1 class="display-4">Welcome to Elemco Software Web Services.</h1>'
    rootString += '<p class="lead">Please select from the following options:</p>'
    rootString += '<ul>'
    rootString += '<li><a href="/plcinfo">PLC Information</a></li>'
    rootString += '<li><a href="/plcinfo/1">PLC Information for PLC ID 1</a></li>'
    rootString += '</ul>'
    return rootString
