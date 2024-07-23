import arcpy
import os

GDB = os.environ.get("DATABASE")
arcpy.env.workspace = GDB
arcpy.env.overwriteOutput = True

class List:
    def __init__(self):
        self.fields = []
        self.edit_field = []
        self.layer_name = "raw_records"

    def listing(self):
        self.fields = arcpy.ListFields(self.layer_name)
        for field in self.fields:
            if field.name == "Shape" or field.name == "OBJECTID" or field.name == "sensor_id" or field.name == "description" or field.name == "X" or field.name == "Y":
                pass
            else:
                self.edit_field.append(field.name)
