import requests
import os

URL = os.environ.get("LINK")

LAYERS_NAME = ["raw_records", "treated_records", "pressure_records"]

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
      print(self.sensors)

  def classify(self):
    for item, value in self.sensors:
      for key in value:
        if key == "rawRecords":
            self.raw.extend(self.sensors[item][key])
            print(self.raw)
        elif key == "treatedRecords":
            self.treated.extend(self.sensors[item][key])
            print(self.treated)
        else:
            self.pressure.extend(self.sensors[item][key])
            print(self.treated)