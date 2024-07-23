# import arcpy
# import os
# import requests
import list
from fetch import Fetch

WTP_NAMES = ["roundpoint", "manshia", "siouf"]

field = list.List()
field.listing()
print(field.edit_field)

ask = Fetch()
for wtp in WTP_NAMES:
  ask.request(wtp)
#   ask.classify()
#env variable
# print("setting env variables----------------------------")
# GDB = os.environ.get("DATABASE")
# URL = os.environ.get("LINK")

# arcpy.env.overwriteOutput = True
# arcpy.env.workspace = GDB

# sensor_fields = []

#listing fields
print("Listing fields------------------------------------")
# fields = arcpy.ListFields("raw_records")
# for field in fields:
#     if field.name == "Shape" or field.name == "OBJECTID" or field.name == "sensor_id" or field.name == "description" or field.name == "X" or field.name == "Y":
#         pass
#     else:
#         sensor_fields.append(field.name) 
# print(sensor_fields)          
# treated = []
# raw = []
# pressure = []

# #request
# print("Requesting API-------------------------------------")
# response = requests.get(URL + "maamoura")
# response.raise_for_status()
# data = response.json()
# sensors = (data["data"])
# print(sensors)

# for item in sensors:
#     if item == "rawRecords":
#         raw.extend(sensors["rawRecords"])
#     elif item == "treatedRecords":
#         treated.extend(sensors["treatedRecords"])
#     else:
#         pressure.extend(sensors["pressureRecords"])

# #editting
# print("Starting Editting----------------------------------")
# edit = arcpy.da.Editor(GDB)
# edit.startEditing(with_undo=False, multiuser_mode=True)
# edit.startOperation()
# for sensor in range(len(raw)): 
#     with arcpy.da.UpdateCursor("raw_records", sensor_fields, f"sensor_id = '{raw[sensor]['TagName']}'") as input_row:
#         for row in input_row:
#             for i in range(len(sensor_fields)):
#                 if raw[sensor]["last_value"] == "0.00":
#                    row[i] = None #continue
#                    input_row.updateRow(row) 
#                 else:
#                    row[i] = (raw[sensor]["last_value"])
#             input_row.updateRow(row)
# edit.stopOperation()
# edit.stopEditing(save_changes=True)
