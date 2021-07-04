import json
dosya=open("mehmet.json","r")
json_dosya=json.load(dosya)
print ("KİMLİK :",json_dosya["kimlik"])

