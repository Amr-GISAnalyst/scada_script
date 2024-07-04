import os
import arcpy
import requests
from dotenv import load_dotenv, dotenv_values

load_dotenv()

#env variable
GDB = os.getenv("DATABASE")
URL = os.getenv("LINK")

arcpy.env.overwriteOutput = True
arcpy.env.workspace = GDB

sensor_fields = []

fields = arcpy.ListFields("rawRecords")
for field in fields:
    if field.name == "Shape" or field.name == "OBJECTID" or field.name == "sensorid" or field.name == "description" or field.name == "x" or field.name == "y":
        pass
    else:
        sensor_fields.append(field.name)       

#Data
treated = []
raw = []
pressure = []

#request
response = requests.get(URL + "roundpoint")
response.raise_for_status()
data = response.json()
sensors = (data["data"])
print(sensors)
#editting
edit = arcpy.da.Editor(GDB)
edit.startEditing(with_undo=False, multiuser_mode=False)
edit.startOperation()
for item in sensors:
    if item == "rawRecords":
        raw.extend(sensors["rawRecords"])
        # print(raw)
        for sensor in range(len(raw)):
             with arcpy.da.UpdateCursor(item,fields,f"raw[sensor]['TagName'] == {'sensorid'}") as input_rows:
                for row in input_rows:
                        for i in range(len(fields)):
                            if raw[i]['last_value'] == "0.00":
                                row[i] = None #continue
                                input_rows.updateRow(row) 
                            else:
                                row[i] = float(raw[i]['last_value'])
                        input_rows.updateRow(row)
edit.stopOperation()
edit.stopEditing(save_changes=True)
