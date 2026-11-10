<!-- This is a Kanban Board file created with MD Kanban extension -->
<!-- GitHub: https://github.com/jebakumarj/md-kanban -->
<!-- VS Code Extension: Search "MD Kanban" in the extension store (ID: jeddak.md-kanban) -->

# Brawl Board

## To Do

#### Krav: spelet börjar
<!-- id: task-1793100000002-2 -->
namnet frågas efter, båda har HP och startvärdena syns. För stort för ett pass, dela upp det i dina egna kort
<!-- priority: high -->
<!-- source: main.py:1 -->

#### Krav: kampen
<!-- id: task-1793100000003-3 -->
båda slår med slumpad skada tills någon har noll HP, i en while med and. En besegrad slår inte tillbaka. Vinnaren skrivs ut. Dela upp det
<!-- priority: high -->

#### Krav: ett val varje tur
<!-- id: task-1793100000004-4 -->
spelaren väljer varje tur, minst två alternativ som du hittar på. Kraschsäkert: katt ger en ny fråga. Dela upp det
<!-- priority: high -->

#### Krav: en for med ett syfte
<!-- id: task-1793100000005-5 -->
se exemplen i readme.md, eller hitta på ett eget syfte
<!-- priority: high -->

#### Fiendens första tankar
<!-- id: task-1793874445518-126 -->
En simpel fiende som bara gör slumpmässiga actions. Se till att det går att expandera till mer intellegens

#### Upkeep
<!-- id: task-1793874527735-160 -->
I början av varje tur, lägg till värden till pengar baserat på ens städer

#### Förlust, eller inte
<!-- id: task-1793874647869-197 -->
Skriv in möjliheten att förlora eller vinna baserat på antalet städer som man har kvar
- [ ] Varabler som förvarar hur många städer man själv respektive ens fiende har kvar

#### Cool transitions
<!-- id: task-1794308094722-273 -->
Om tid finns: Lägg till så att varje gång en karaktär ändras att den går genom ett stadie av nonsens för att det ska se coolare ut. Lite static effekt typ

## In Progress

#### Planera och skriv dina kort
<!-- id: task-1793100000001-1 -->
planering.md: ditt spel, planen och dina kort. Lägg in korten här. Visa läraren innan du skriver kod
<!-- priority: critical -->
<!-- source: planering.md:1 -->

#### Krav: readme och faserna
<!-- id: task-1793100000006-6 -->
rubrikerna längst ner i readme.md. faser.md fylls i längs vägen och blir klar sist
<!-- priority: high -->
<!-- source: faser.md:1 -->

#### Spelarens tur
<!-- id: task-1793874385785-95 -->
Använd väljsystemet för att låta spelaren välja vilken stad och vad man ska göra där
- [ ] Välj action på en stad och utför det

#### Handle_command metod
<!-- id: task-1794318935952-316 -->
Metod som tar in ett kommando från spelaren (via väljsystemet) och utför det

## Done

#### Forka repot
<!-- id: task-1793100000000-0 -->
forka och klona repot, öppna det i VS Code

#### Grunderna (variablar)
<!-- id: task-1793874255151-42 -->
Skriv variabler som  förvarar de viktiga värdena,
pengar, attackstyrka och städerna
- [x] Skapa en klass eller liknande för vilket stadie städerna är i

#### Väljsystemet
<!-- id: task-1793874326218-67 -->
Ett sätt att välja vilken stad man vill ha
- [x] Displaymetod för städerna
- [x] Metod som returnerar rätt ascii baserat på stadens stadie
