import requests
import arcpy
import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()

class Scada:
    def __init__(self):
        self.DATABASE = os.getenv("GDB")
        self.URL = os.getenv("URI")
        self.arc_env()

    def arc_env(self):
        arcpy.env.overwriteOutput = True
        arcpy.env.workspace = self.DATABASE

    def pr(self):
        print(self.DATABASE)
        print(self.URL)

    def request(self):
        response = requests.get(self.URL + "roundpoint")
        response.raise_for_status()
        data = response.json()
        print(data)