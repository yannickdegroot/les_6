mijn_lijst = ["appel", "banaan", "citroen",]
#Een list begint met een variable, in dit geval "mijn_lijst"
#Aan de variable worden meerdere elementen gekoppeld.
#De elementen kunnen strings, integers, floats, booleans of een combinatie hiervan zijn.
#De elementen van een list staan tussen rechte haken: [].
#De elementen worden gescheiden door komma's.
#Ieder element heeft een eigen index, beinnend bij 0

keuze = mijn_lijst[1]
print(keuze)
#De gewenste index wordt tussen rechte haken [] na de naam van de list aangegeven.
#"banaan" heeft de index [1]

keuze = mijn_lijst[-1]
print(keuze)
#"citroen" heeft de index [2] of [-1]

mijn_lijst2 = ["Ma", "Di", "Wo", "Do", "Vr", "Za", "Zo"]

print(mijn_lijst2[2:5])
#De dubbele punt : betekend tot, en niet t/m.
#In dit voorbeeld worden de elementen met index [2 tot 5] geprint

print(mijn_lijst2[5:])
#Wanneer je geen eind aangeeft na de dubbele punt :, dan stopt het printen automatisch aan het einde van de list.

mijn_lijst3 = ["Wafels", "Softijst", "Schepijs", "Pannenkoeken"]

for item in mijn_lijst3:
    print(f"Wij verkopen", item)
#Hiermee voeg je een iteratie (loop) toe aan de list.
#Elke item in de list wordt hierdoor na elkaar geprint.
#De f voor de string, betekend dat het een formatted string is.
#Bij een formated string begrijpt de Python Interpreter dat alle elementen tussen {}, variabelen zijn.

mijn_lijst3.append("Muffins")
#Je kunt verschillende methodes toevoegen aan een object.
#Het object in dit geval is "mijn_lijst3".
#De methode is ".append".
#Met de append methode, voeg je elementen toe aan het einde van de list.

for item in mijn_lijst3:
    print(f"Wij verkopen", item)

mijn_lijst4 = ["A", "B", "D", "E", "F"]

mijn_lijst4.insert(2, "C")
#Met de methode .insert, kun je elementen in het midden van de list toevoegen op de plek die je aangeeft met de index.
#Met de index 2 wordt aangegeven dat je het element C wilt toevoegen voor het element met de index 2.

print(mijn_lijst4)

mijn_lijst5 = ["appel", "banaan", "kers"]

mijn_lijst5.pop(1)
#Met de methode .pop, kun je elementen uit de list verwijderen door de index van het te verwijderen element aan te geven.

print(mijn_lijst5)

mijn_lijst5.remove("appel")
#Met de methode .remove, kun je elementen uit de list verwijderen door de naam van het te verwijderen element aan te geven.

print(mijn_lijst5)

'''Overzicht beschikbare methodes:
.append() - Voegt een element toe aan het eind van de list.
.insert() - Voegt een element toe vóór de plaats met de gespecificeerde index.
.pop() - Verwijdert het element met de hespecificeerde index.
.remove() - Verwijdert het eerste element met de gespecificeerde waarde.
.clear() - Verwijdert alle elementen uit de list.
.copy() - Maakt een kopie van de list.
.count() - Telt het aantal elementen in de list met een bepaalde waarde.
.extend() - Voegt een list toe aan de bestaande list.
.index() - Geeft de index van het eerste element dat gelijk is aan een bepaalde waarde.
.reverse() - Draait de volgorde van de list om.
.sort() - Sorteert de list alfabetisch.'''