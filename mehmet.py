import json
dosya=open("mehmet.json","r")
json_dosya=json.load(dosya)
print ("ADI :",json_dosya["kimlik"].get("Ad"))
print ("SOYADI :",json_dosya["kimlik"].get("Soyad"))
