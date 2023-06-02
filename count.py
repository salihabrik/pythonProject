
countries ={}
countries ["Algeria"] =100
countries ["KSA"] = 25
countries ["USA"]= 200
print(countries)
countries ["Algeria"]= 333
print(countries)
print(len(countries))
print("tunis" in countries)
d1 = {"mike" :33,"bob":44,"hih":22}
d2 = {"mike" :33,"bob":44,"hih":22}
print (d1 == d2)
print(countries.get("Algeria"))
print(countries.get("Alge","not exist"))
for k in countries.values():
    print(k)