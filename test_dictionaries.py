mijn_dictionary1 = {
    "merk" : "Mitsubishi",
    "model" : "Colt",
    "bouwjaar" : 2010,
    "kleur" : "blauw",
    "staat" : "gebruikt"
}
#Een dictionary begint met een variable, in dit geval "mijn_dictionary1".
#Een dictionary bestaat uit keys en values.
#Deze keys en values staan aangegeven tussen {}.
#De keys en bijbehorende values worden gescheiden met een :.
#Je eindigt een key en value met een komma, voordat je naar een nieuwe key en value gaat.
#De keys in een dictionary moeten uniek zijn.

print(mijn_dictionary1)
#Om de gehele dictionary in een keer te printen.

mijn_dictionary2 = {
    "product" : "softijs",
    "aantal" : 101,
    "smaak" : "vanille"
}

print(mijn_dictionary2["aantal"])
#Tegenovergestelde als bij een list, benoem je bij een dictionary de key die je wilt printen.
#Een dictionary heeft geen index

variabele1 = mijn_dictionary2.keys()
print(variabele1)
#Om alle keys te binden aan 1 variabele gebruik je deze code.
#Je begint met het aangeven van de variabele.
#Je verwijst daarna naar de naam van de dictionary.
#Je voegt de .keys() methode toe aan de dictionary.
#Het is niet mogelijk om waardes tussen de () in de .keys methode aan te geven.

variabele2 = mijn_dictionary2.values()
print(variabele2)
#Om alle values te binden aan 1 variabele gebruik je deze code.
#Je begint met het aangeven van de variabele.
#Je verwijst daarna naar de naam van de dictionary.
#Je voegt de .values() methode toe aan de dictionary.
#Het is niet mogelijk om waardes tussen de () in de .values methode aan te geven.

variabele3 = mijn_dictionary2.items()
print(variabele3)
#Om zowel alle keys als alle values te binden aan 1 variabele gebruik je deze code.
#Je begint met het aangeven van de variabele.
#Je verwijst daarna naar de naam van de dictionary.
#Je voegt de .items() methode toe aan de dictionary.
#Het is niet mogelijk om waardes tussen de () in de .items methode aan te geven.

for item in mijn_dictionary2:
    print(item)
#Hiermee voeg je een iteratie (loop) toe aan de dictionary
#Hiermee worden de keys in de dictionary als iteratie geprint

for item in mijn_dictionary2:
    print(mijn_dictionary2[item])
#Hiermee voeg je een iteratie (loop) toe aan de dictionary
#Hiermee worden de values in de dictionary als iteratie geprint

for k, v in mijn_dictionary2.items():
    print(k, v)
#Met de methode .items(), benoem je zowel de keys als de values.
#De k staat voor key, de v staat voor value. Beide kunnen ook voluit geschreven worden.
