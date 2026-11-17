## [Datum] – [Kort titel på problemet]

**Vad gick fel:**
[Beskriv problemet konkret]

**Varför:**
[Din analys av grundorsaken. Skriv den innan du frågar AI]

**Hur jag löste det:**
[Vad du faktiskt gjorde]

**Vad jag skulle göra annorlunda:**
[Din reflektion – det viktigaste fältet]

**AI (om du frågade):**
[Prompten, vad AI föreslog, vad du ändrade och vad AI missade]



12 NOV
Fiendeturen startar aldrig
Fixad genom att starta den i while-loopen som styr spelet
Glöm ba inte att lägga till det


17 NOV
Crashar slumpmässigt efter att man väljer action.
Det visa sig att när game staget gick till upkeep fanns det inget sätt att komma ut, därför la jag till en linje som skickar vidare spelet när det händer.
Var slarv egentligen, inge mer.