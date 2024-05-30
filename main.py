import requests
import os
import arcpy
from dotenv import load_dotenv, dotenv_values
#----------------------------------------------
load_dotenv()
#----------------------------------------------
# setting env variables for AUTH to use it safely.
print("setting env variables for AUTH to use it safely.\n ---------------------------------------")
#---------------------------------------------------------------
URI = os.getenv("URL")

response = requests.get(url=URI+"manshia_2")
response.raise_for_status()
data = response.json()
print(data)