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
