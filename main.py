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

fields = arcpy.ListFields("GIS.APP_Features\\GIS.rawRecords")
for field in fields:
    if field.name == "Shape" or field.name == "OBJECTID" or field.name == "sensorid" or field.name == "description" or field.name == "X" or field.name == "Y":
        pass
    else:
        sensor_fields.append(field.name)       
# print(sensor_fields)
#Data
treated = []
raw = []
pressure = []

#request
response = requests.get(URL + "roundpoint")
response.raise_for_status()
data = response.json()
sensors = (data["data"])
# print(sensors)

for item in sensors:
    if item == "rawRecords":
        raw.extend(sensors["rawRecords"])
    elif item == "treatedRecords":
        treated.extend(sensors["treatedRecords"])
    else:
        pressure.extend(sensors["pressureRecords"])

#editting
edit = arcpy.da.Editor(GDB)
edit.startEditing(with_undo=False, multiuser_mode=True)
edit.startOperation()
for sensor in range(len(raw)):
    for tag in raw[sensor]["TagName"]:
        with arcpy.da.UpdateCursor(in_table= "GIS.APP_Features\\GIS.rawRecords", field_names= sensor_fields, where_clause= f"sensorid = {tag}") as data_edit:
            for row in data_edit:
                for i in range(len(sensor_fields)):
                    if raw[sensor]["last_value"] == "0.00":
                        row[i] = None #continue
                        data_edit.updateRow(row) 
                    else:
                        row[i] = float(raw[sensor]["last_value"])
                data_edit.updateRow(row)
edit.stopOperation()
edit.stopEditing(save_changes=True)
