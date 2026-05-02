dc = {"alice": 162, "bob": 178, "carol": 155}
print(dc)
print(dc["alice"])
print(dc["bob"])
print(dc["carol"])
print(dc.keys())
print(dc.values())
print(dc.items())
for key, value in dc.items():
    print(key, value)
