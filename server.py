import list
from fetch import Fetch

WTP_NAMES = ["roundpoint", "manshia", "siouf"]

field = list.List()
field.listing()
print(field.edit_field)

ask = Fetch()
for wtp in WTP_NAMES:
  ask.request(wtp)

ask.edit() 

print("operation Success.")