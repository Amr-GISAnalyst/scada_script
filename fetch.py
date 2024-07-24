import requests
import os
import arcpy
from list import edit_field

GDB = os.environ.get("DATABASE")
URL = os.environ.get("LINK")

LAYERS_NAME = ["raw_records", "treated_records", "pressure_records"]
raw = []
treated = []
pressure = []

class Fetch:
  def __init__(self):
    self.sensors = {"roundpoint":0 ,"manshia":0 ,"siouf":0}
    self.raw = []
    self.treated = []
    self.pressure = []
    
  def request(self,wtp): 
      response = requests.get(URL + wtp)
      response.raise_for_status()
      data = response.json()
      self.sensors[wtp] = data["data"]

  def edit(self):
    edit = arcpy.da.Editor(GDB)
    edit.startEditing(with_undo=False, multiuser_mode=True)
    edit.startOperation()
    for layer in LAYERS_NAME:
        if layer == "raw_records":
          for wtp in self.sensors:
            self.session(raw,wtp,"rawRecords","raw_records")
        elif layer == "treated_records":
          for wtp in self.sensors:
            self.session(treated,wtp,"treatedRecords","treated_records")
        elif layer == "pressure_records":
          for wtp in self.sensors:
            self.session(pressure,wtp,"pressureRecords","pressure_records")
    edit.stopOperation()
    edit.stopEditing(save_changes=True)

  def session(self,data,api_name,type,layer):
    data.extend(self.sensors[api_name][type]) 
    for sensor in range(len(data)): 
      with arcpy.da.UpdateCursor(layer, edit_field, f"sensor_id = '{data[sensor]['TagName']}'") as input_row:
          for row in input_row:
              for i in range(len(edit_field)):
                  # if data[sensor]["last_value"] == "0.00":
                  #   row[i] = None #continue
                  #   input_row.updateRow(row) 
                  # else:
                row[i] = (data[sensor]["last_value"])
              input_row.updateRow(row)  