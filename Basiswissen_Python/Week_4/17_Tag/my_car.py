mein_auto = {
    "marke": "Opel",
    "baujahr": "2025",
    "kilometer": 10_000
    }

print(mein_auto["marke"])

for key in mein_auto.keys():
    print(key)
    
print(f"Mein Auto ist ein {mein_auto["marke"]} und hat {mein_auto["kilometer"]} kilometer darauf.")