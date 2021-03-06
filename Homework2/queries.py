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

sameCitySupps = {tuple(sorted((s[1], d[1]))) for s in parts.suppliers
                                             for d in parts.suppliers
                                             if d[3] == s[3] if d[1] != s[1]}
print(sameCitySupps)

suppByCity = {s[3] : {d[1] for d in parts.suppliers if d[3] == s[3]} for s in parts.suppliers}
print(suppByCity)
