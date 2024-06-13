import requests
import os
import arcpy
from Scada import Deploy
#----------------------------------------------
from dotenv import load_dotenv, dotenv_values
#----------------------------------------------

#----------------------------------------------
# setting env variables for AUTH to use it safely.
print("setting env variables for AUTH to use it safely.\n ---------------------------------------")
#---------------------------------------------------------------
#listing fields in 3 featureclasses.
print("listing fields in both featureclasses.\n ---------------------------------------")
#------------------------------------------

raw = Deploy("rawRecords")
raw.request_data("manshia")