#team = ["Sare","Yasaman","Fadi","Niko","Thomas"]

# print jeden Teilnehmer ausser Niko

for member in ["Sare","Yasaman","Fadi","Niko","Thomas"]:
    if member == "Niko":
        continue
    print(member)
    
for member in ["Sare", "Meyer", "Yasaman","Fadi","Niko","Thomas", "Maier", "Mayer"]:
    if "y" in member.lower():
        print(member, "contains y")
        print(len(member), "Buchstaben")