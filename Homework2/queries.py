import parts
boltSupps = {s[1] for s in parts.suppliers
                  for r in parts.spj
                  for p in parts.parts
                  if r[0] == s[0] if p[0] == r[1] if p[1] == 'Bolt'}
print(boltSupps)

colorSupps = {s[1] for s in parts.suppliers
                   for r in parts.spj
                   for p in parts.parts
                   if r[0] == s[0] if p[0] == r[1] if p[2] == 'Red'}
print(colorSupps)

sameCitySupps = {(s[1], d[1]) for s in parts.suppliers
                              for d in parts.suppliers
                              if d[3] == s[3] if d[1] != s[1]}

# pair = ()
# mySet = set()
# for city in parts.suppliers:
#     for place in parts.suppliers:
#         if place[3] == city[3] and place [1] != city[1]:
#             pair = city[1], place[1]
#             if pair[::-1] not in mySet:
#                 mySet.add(pair)

print(sameCitySupps)

suppByCity = {s[3] : {s[1], d[1]} for s in parts.suppliers
                                  for d in parts.suppliers
                                  if d[1] != s[1] if d[3] == s[3]}

# supCity = dict()
# for s in parts.suppliers:
#     supCity.setdefault(s[3],set()).add(s[1])
print(suppByCity)
