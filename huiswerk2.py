Persoonlijke_Gegevens = {
    "Voornaam" : "Harry",
    "Achternaam" : "van Winkel",
    "Geboortedatum" : "27-3-1939"
}

for k, v in Persoonlijke_Gegevens.items():
    print(k, v)

print()
print(Persoonlijke_Gegevens["Voornaam"])

Persoonlijke_Gegevens["Voornaam"] = "Henrikus"
print()
for k, v in Persoonlijke_Gegevens.items():
    print(k, v)