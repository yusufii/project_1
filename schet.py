d = {}

line = text
for litera in line:
  counter = d.get(litera,0)
  counter += 1
  d[litera] = counter
for key in d.keys():
  print(key,"-",d[key])