import arcpy
import requests
import os
from dotenv import load_dotenv, dotenv_values


DATABASE = os.getenv("GDB")
arcpy.env.overwriteOutput = True
arcpy.env.workspace = DATABASE


class Deploy:
    def __init__(self,featureclass):
        self.URI = os.getenv("URL")
        
        load_dotenv()
        self.end_wtp = {
        "roundpoint": "RondPoint",
        "manshia": "Manshia",
        "manshia_2": "Manshia2",
        "siouf": "Siouf",
        "maamoura": "Maamoura",
        "nozha": "Nozha",
        "k40": "BA"}

        self.fields = []

        list = arcpy.ListFields(featureclass)
        for field in list:
            if field.name == "Shape" or field.name == "OBJECTID" or field.name == "sensor_id" or field.name == "wtp_name" or field.name == "description":
                pass
            else:
                self.fields.append(field.name)

    def request_data(self,dict_code):
        response = requests.get(self.URI + (dict_code))
        response.raise_for_status()
        data = response.json()
        print(data)