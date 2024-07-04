import os
import arcpy
import requests
from dotenv import load_dotenv, dotenv_values
load_dotenv()

#env variable
GDB = os.getenv("DATABASE")
URL = os.getenv("LINK")

arcpy.env.workspace = GDB
arcpy.env.overwriteOutput = True

#Data
treated = []
raw = []
pressure = []

#request
response = requests.get(URL + "roundpoint")
response.raise_for_status()
data = response.json()
sensors = (data["data"])

fields = []
fields = arcpy.ListFields(GDB + "\\" +"pressureRecords")
for field in fields:
    if field.name == "Shape" or field.name == "OBJECTID" or field.name == "sensorid" or field.name == "description" or field.name == "GlobalID" or field.name == "x" or field.name == "y":
        pass
    else:
        fields.append(field.name)

#editting
for item in sensors:
    if item == "rawRecords":
        raw.extend(sensors["rawRecords"])
        # print(raw)
        for i in range(len(raw)):
             with arcpy.da.UpdateCursor(item,fields,f"raw[i]['TagName'] = {'sensorid'}") as input_rows:
                for row in input_rows:
                        for i in range(len(fields)):
                            if raw[i]['last_value'] == "0.00":
                                row[i] = None #continue
                                input_rows.updateRow(row) 
                            else:
                                row[i] = float(raw[i]['last_value'])
                        input_rows.updateRow(row)

#     elif item == "treatedRecords":
#         treated.extend(sensors["treatedRecords"])
#         print(treated)
#     else:
#         pressure.extend(sensors["pressureRecords"])
#         print(pressure)

# print(sensors)