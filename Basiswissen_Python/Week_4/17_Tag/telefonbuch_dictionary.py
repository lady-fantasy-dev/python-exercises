# ============================================
# Übung: Dictionaries vertieft
# ============================================

telefonbuch = {
    "Anna": "0711-123456",
    "Peter": "0721-456789",
    "Niko": "07751-987654",
    "Sarah": "0761-222333",
    "Thomas": "01728965664",
    "Sare": "01728949364",
    "Yasmine": "01723563364",
    "Fadi": "01725763364"
}

# Aufgabe 1
# Gib alle Namen aus.

for keys in telefonbuch.keys():
    print(f"the keys are {keys}")

# Aufgabe 2
# Gib alle Telefonnummern aus.

for values in telefonbuch.values():
    print(f"the values are {values}")

# Aufgabe 3
# Gib Namen UND Telefonnummer aus.
#
# Verwende items().

for values in telefonbuch.items():
    print(f"the keys are {keys} & the values are {values}")
    
# Aufgabe 4
# Prüfe, ob "Niko" vorhanden ist.

if "Niko" in telefonbuch.keys():
    print("Niko exists")

# Aufgabe 5
# Verwende get(), um die Nummer
# von "Max" abzurufen.

print(f"Max: {telefonbuch.get("Max")}")

#
# Wenn Max nicht vorhanden ist,
# soll "nicht vorhanden" ausgegeben werden.

if "Max" not in telefonbuch.keys():
    print("nicht vorhanden")

# Aufgabe 6
# Füge "Max" hinzu.

telefonbuch.update({"Max": ""})

# alternative:
# telefonbuch["Max"] = "021545458"

print(telefonbuch)


# Aufgabe 7
# Ändere die Telefonnummer von Anna.

telefonbuch.update({"Anna": "567564"})

# alternative
#telefonbuch["Anna"] = "4646453"

print(telefonbuch)

# Aufgabe 8
# Entferne Sarah mit pop().

telefonbuch.pop("Sarah")
print(telefonbuch)

# Aufgabe 9
# Gib die Anzahl der Personen aus.
print(len(telefonbuch))

# Aufgabe 10
# Gib nur Personen aus, deren
# Name mit "S" beginnt.

for key in telefonbuch.keys():
# for key in telefonbuch:
    if "S" in key:
        print(key)
        
# Suche nach Leuten, die in der Telefonnummer eine 5 haben

for value in telefonbuch.values():
    if "5" in value:
        print(value)
        
# Print the names of the people whose number contains a 5

for key, value in telefonbuch.items():
    if "5" in value:
        print(key)

