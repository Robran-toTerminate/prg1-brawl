# Planering

Planera innan du skriver kod. Här bestämmer du vad ditt spel ska vara, hur kampen fungerar och
vilka kort du bygger det med. Visa planen och korten för läraren innan du börjar koda.

Planen är att det är en kamp mellan två länder om vem som kan förstöra alla den andres

## Mitt spel

Kraven är samma för alla. Vad gör ditt spel till ditt? Vem är du, vem slåss du mot, och var? Vad
kan spelaren välja mellan varje tur? Finns det en regel som bara ditt spel har?

Skriv några meningar. Idén får ändras längs vägen, och då skriver du vad du ändrade i faser.md.


Ideen är att två länder ska strida mot varandra. Man väljer en stad på sin tur och gör en tillhörande action. T.ex att bygga en fabrik eller attackera en fiende. Den som först förlorar alla sina städer förlorar.


## Fyra frågor planen ska svara på

Tänk igenom dessa steg på samma sätt som vi har gjort spårningen tillsammans på tavlan. Vilka variabler behöver du? Vilka villkor? Vad ska de göra? Vad sker i nästa steg/rad?

1. Var börjar programmet, och vad finns innan första turen?
2. Vad händer inuti en tur, i vilken ordning?
3. Vad avgör om det blir en tur till?
4. Vad händer efter sista turen?

## Min plan

Rita ett flödesschema på papper och lägg in ett foto här, eller skriv pseudokod: programmets steg
med vanliga ord, en rad per steg, utan att bry dig om Python.

(Foto av flödesschemat, eller pseudokoden.)

se psudokod.txt

Jag ska också sträva efter att skriva på ett vis som ger mig möjligheten att implementera pygame i framtiden.

## Mönster jag tror att jag behöver

Gå igenom Mönsterkortet med planen framför dig. Vilka mönster känner du igen?

-Att det finns en stor loop där spelaren gör sina val innan spelet kollar ifall fienden har förlorat. Först efter att spelaren har fått en chans att vinna får fienden sin tur.

## Mina kort

Kravkorten på brädet säger _vad_ spelet ska klara. De är för stora med flit, och du gör om dem till
dina egna kort, de som säger _hur_ du bygger det. Två sorters kort:

- **Delar av kraven.** Varje kravkort blir några mindre kort.
- **Mitt spel.** Minst två kort med dina egna idéer från första rubriken.

Ett bra kort ryms i en lektion, slutar med något du kan köra och se, och har ett namn som duger som
commitmeddelande. Exempel:

> **Slumpad skada:** spelarens skada slumpas mellan 5 och 15. Kör fem gånger, skadan ska variera.

"Gör kampen" är inget kort, det är fem. Vet du inte hur du ska dela upp kampen, titta på stegen på
kurswebben och gör dem till dina kort.

Skriv listan här och skapa korten efteråt, eller direkt som kort.

- a
- b
