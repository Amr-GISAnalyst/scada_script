import arcpy
import os
import requests
#env variable
print("setting env variables----------------------------")
GDB = os.environ.get('DATABASE')
URL = os.environ.get('LINK')

arcpy.env.overwriteOutput = True
arcpy.env.workspace = GDB

sensor_fields = []

#listing fields
print("Listing fields------------------------------------")
fields = arcpy.ListFields("rawRecords")
for field in fields:
    if field.name == "Shape" or field.name == "OBJECTID" or field.name == "sensorid" or field.name == "description" or field.name == "X" or field.name == "Y":
        pass
    else:
        sensor_fields.append(field.name)       
print(sensor_fields)

treated = []
raw = []
pressure = []

#request
print("Requesting API-------------------------------------")
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
print("Starting Editting----------------------------------")
edit = arcpy.da.Editor(GDB)
edit.startEditing(with_undo=False, multiuser_mode=True)
edit.startOperation()
for sensor in range(len(raw)):
    tg = raw[sensor]["TagName"]
print(tg)    
#     with arcpy.da.UpdateCursor("sensors\\rawRecords", sensor_fields, f"sensorid = {tg}") as data_edit:
#         for row in data_edit:
#             for i in range(len(sensor_fields)):
#                 if raw[sensor]["last_value"] == "0.00":
#                     row[i] = None #continue
#                     data_edit.updateRow(row) 
#                 else:
#                     row[i] = float(raw[sensor]["last_value"])
#             data_edit.updateRow(row)
# edit.stopOperation()
# edit.stopEditing(save_changes=True)
