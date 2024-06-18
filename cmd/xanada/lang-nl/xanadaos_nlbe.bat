@echo off
color 3B

:login
cls
title XANADA OS 1.0
echo Welkom bij XANADA OS 1.0!
echo Gemaakt door Sapero voor 2019
echo Wil je inloggen?
echo 1) Ja
echo 2) Nee
set /p login0=C:\

if %login0% == 1 goto name
if %login0% == 2 goto savecheck
goto login

:savecheck
echo Heb jij een save?
echo 1) Ja
echo 2) Nee
set /p login1=C:\

if %login1% == 1 goto desktop1
if %login1% == 2 goto name
goto savecheck

:name
cls
echo Wat is je naam?
set /p name=C:\
goto start

:start
cls
echo Hallo %name%!
echo Wil je naar de desktop?
echo 1) Ja
echo 2) Nee
set /p choice1=C:\

if %choice1% == 1 goto desktop1
if %choice1% == 2 exit
exit

:desktop1
cls
color 3B
echo Welkom bij the desktop. Wat wil je doen?
echo 1) Rekenmachine
echo 2) Kalender
echo 3) Browser
echo 4) Memory
echo 5) Meer
set /p choice2=C:\

if %choice2% == 1 goto calculator
if %choice2% == 2 goto calender
if %choice2% == 3 goto browser
if %choice2% == 4 goto memorystart
if %choice2% == 5 goto desktop2
goto desktop1

:calculator
cls
echo Welkom bij Rekenmachine! Alleen een 32-Bit basis.
echo Druk 1 voor Additie
echo Druk 2 voor Subtractie
echo Druk 3 voor Multiplicatie
echo Druk 4 voor Divisie
echo Druk 5 om terug te gaan
set /p type=

if %type%== 1 goto add
if %type%== 2 goto sub
if %type%== 3 goto mul
if %type%== 4 goto div
if %type%== 5 goto desktop1
goto calculator

:add
echo.
echo Additie
echo Kies 2 nummers die je wilt optellen
set /p num1=
set /p num2=
echo %num1%+%num2%?
pause
set /a Answer=%num1%+%num2%
echo %Answer%
pause
goto calculator

:sub
echo.
echo Subtractie
echo Kies 2 nummers die je wilt aftrekken
set /p num1=
set /p num2=
echo %num1%-%num2%?
pause
set /a Answer=%num1%-%num2%
echo %Answer%
pause
goto calculator

:mul
echo.
echo Multiplicatie
echo Kies 2 nummers die je wilt multipliceren
set /p num1=
set /p num2=
echo %num1%*%num2%?
pause
set /a Answer=%num1%*%num2%
echo %Answer%
pause
goto calculator

:div
echo Divisie
echo Kies 2 nummers die je wilt delen
set /p num1=
set /p num2=
echo %num1%/%num2%?
pause
set /a Answer=%num1%/%num2%
echo %Answer%
pause
goto calculator

:calender
cls
echo Welkom bij Kalender!
echo Datum: %date% Tijd: %time%
pause
goto desktop1

:browser
cls
echo Welkom bij Browser!
echo Je kan de hele dag surfen!
echo Ben je klaar?
pause
goto sites

:sites
cls
echo 1) Google
echo 2) Bing
echo 3) Yahoo
echo 4) DuckDuckGo
echo 5) Yandex
set /p choice3=C:\
if %choice3% == 1 goto google
if %choice3% == 2 goto bing
if %choice3% == 3 goto yahoo
if %choice3% == 4 goto duckduckgo
if %choice3% == 5 goto Yandex
goto sites

:google
cls
echo Google
pause
start www.google.com
goto desktop1

:bing
cls
echo Bing
pause
start www.bing.com
goto desktop1

:yahoo
cls
echo Yahoo
pause
start www.yahoo.com
goto desktop1

:duckduckgo
cls
echo DuckDuckGo
pause
start www.duckduckgo.com
goto desktop1

:yandex
cls
echo Yandex
pause
start www.yandex.com
goto desktop1

:memorystart
cls
echo Welkom bij Memory!
echo Wil je starten?
echo 1) Ja
echo 2) Nee
set /p choice4=C:\

if %choice4% == 1 goto memoryquestion
if %choice4% == 2 goto desktop1
goto memorystart

:memoryquestion
cls
echo Je hebt 3 nummers:
echo 1) %random%
echo 2) %random%
echo 3) %random%
echo Ben je klaar?
pause
cls
echo Welk nummer was nummer 2?
set /p choice5=C:\

if %choice5% == %number2% goto memorywin
if %choice5% == Not %number2% goto memorywrong

:memorywin
cls
echo Je hebt het juist!
echo Je wint het spel!
pause
goto desktop1

:memorywrong
cls
echo Je hebt het fout!
echo Opnieuw?
pause
goto memorystart

:desktop2
cls
echo 1) Afsluiten
echo 2) Herstarten
echo 3) Antivirus (GRAP)
echo 4) Notitie
echo 5) Bekijk notitie
echo 6) Terug
echo 7) Meer
set /p choice6=C:\

if %choice6% == 1 goto shutdown1
if %choice6% == 2 goto restart1
if %choice6% == 3 goto antivirus1
if %choice6% == 4 goto write1
if %choice6% == 5 goto viewwrite1
if %choice6% == 6 goto desktop1
if %choice6% == 7 goto desktop3
goto desktop2

:shutdown1
cls
echo Wil je echt afsluiten?
echo 1) Ja
echo 2) Nee
set /p choice7=C:\

if %choice7% == 1 goto shutdown2
if %choice7% == 2 goto desktop1
goto shutdown1

:shutdown2
cls
echo Afsluiten...
ping 10 9 8 7 6 5 4 3 2 1
exit

:restart1
cls
echo Ben je zeker dat je wilt herstarten?
echo 1) Ja
echo 2) Nee
set /p choice8=C:\

if %choice8% == 1 goto restart2
if %choice8% == 2 goto desktop1
goto restart1

:restart2
cls
echo Herstarten...
ping 10 9 8 7 6 5 4 3 2 1
goto login

:antivirus1
cls
echo Welkom bij XANADA Antivirus
echo OPGELET! DIT IS EEN GRAP! NEEM DIT NIET SERIEUS!!!!!!!!!!!!!!!!!!!
if exist virus.exe goto antivirusvirus
if Not exist virus.exe goto antivirusnone

:antivirusvirus
echo.
echo Oppassen! Virus gevonden!
pause
del virus.exe
goto desktop1

:antivirusnone
echo.
echo Je computer is veilig!
pause
goto desktop1

:write1
cls
echo Welkom bij Notitie!
echo Hier kan je notities schrijven.
echo Wil je een nieuwe notitie maken?
echo 1) Ja
echo 2) Nee
set /p choice9=C:\

if %choice9% == 1 goto write2
if %choice9% == 2 goto desktop1
goto write1

:write2
cls
echo Hoe noem je de notitie?
set /p filename=C:\
echo Welke text wil je in uw notitie?
set /p text=C:\
echo Notitie gecreëerd!
echo Om uw notitie te bekijken, ga naar Notitie bekijken op het desktop.
pause
goto desktop1

:viewwrite1
cls
echo Welkom bij Notitie.
echo Je notities:
echo 1) %filename%
echo Wil je je notitie bekijken?
echo 1) Ja
echo 2) Nee
set /p choice10=C:\

if %choice10% == 1 goto viewwrite2
if %choice10% == 2 goto desktop1

:viewwrite2
cls
echo Notietienaam:
echo %filename%
echo Text:
echo %text%
pause
goto desktop1

:desktop3
cls
echo 1) Quiz
echo 2) Zombie Gevecht
echo 3) Matrix
echo 4) Terug
echo 5) Meer
set /p choice11=C:\

if %choice11% == 1 goto quiz
if %choice11% == 2 goto zombiefight
if %choice11% == 3 goto matrix
if %choice11% == 4 goto desktop2
if %choice11% == 5 goto desktop4
goto desktop3

:quiz
cls
echo OK dan, eerste vraag. Hoeveel landen zijn er in het Verenigd Koninkrijk?
set /p choice12=C:\

if %choice12% == 3 goto quizanswerright
if %choice12% == 4 goto quizanswermisconception1
if %choice12% == 2 goto quizanswermisconception2
cls
echo Fout! Niet eens kort!
echo 1) Opniew
set /p choice12=C:\

if %choice12% == 1 goto quiz

:quizanswerright
cls
echo Jij zijt een legende maat! Noord Ierland is gewoon een provincie! Sorry dat was een trukvraag.
pause
goto quiz

:quizanswermisconception1
cls
echo Ehhh... Kortbij. Dat is een misconceptie. Er zijn geen '4' Landen in de VK. Noord Ierland is gewoon een provincie.
echo 1) Opnieuw
set /p choice13=C:\

if %choice13% == 1 goto quiz
cls
echo Kan je één van de nummers kiezen, dat zou ECHT helpen.
echo 1) Terug
set /p choice13=C:\

if %choice13% == 1 goto quizanswermisconception1

:quizanswermisconception2
cls
echo Ehhh... Kortbij. Dat is een misconceptie. Er zijn geen '2' Landen in de VK. Groot Britanië is een eiland, niet een land!
echo 1) Opnieuw
set /p choice14=C:\
if %choice14% == 1 goto quiz
cls
echo Kan je één van de nummers kiezen, dat zou ECHT helpen.
echo 1) Terug
set /p choice14=C:\
if %choice14% == 1 goto quizanswermisconception2

:zombiefight
cls
echo Oh Nee, er komt een zombie naar jou to!
echo Wat ga je doen!?
echo 1) Boksen
echo 2) Stampen
set /p choice15=C:\

if %choice15% == 1 goto punch
if %choice15% == 2 goto kick
goto zombiefight

:punch
echo Je gebruikt Boksen!
echo Zombie gebruikt Bijt!
echo Uw HP is Nu: 7
echo Zombie's HP is Nu: 3
echo Wat ga je doen?
echo 1) Stampen
set /p choice16=C:\

if %choice16% == 1 goto zombiekill
goto punch

:kick
echo Jij gebruikt Stampen!
echo Zombie gebruikt Bijt!
echo Uw HP is Nu: 7
echo Zombie's HP is Nu: 5
echo Wat ga je doen?
echo 1) Boksen
set /p choice17=C:\

if %choice17% == 1 goto zombiekill
goto kick

:zombiekill
cls
echo Goed gedaan!
echo Je hebt de zombie vermoord!
pause
goto desktop1

:matrix
@echo off
color 0a
echo %random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%
goto matrix

:desktop4
cls
echo 1) Open Applicaties
echo 2) Virus
echo 3) Clicker
echo 4) Bugs
echo 5) Tekeningen
echo 6) Ga Terug
echo 7) Meer
set /p choice18=C:\

if %choice18% == 1 goto openapps
if %choice18% == 2 goto virus
if %choice18% == 3 start xanadaclicker_nlbe.vbs
if %choice18% == 4 goto buglog
if %choice18% == 5 goto drawings
if %choice18% == 6 goto desktop3
if %choice18% == 7 goto desktop5
goto desktop4

:openapps
cls
echo 1) Kladblok
echo 2) Go back
set /p choice19=C:\

if %choice19% == 1 start notepad.exe
if %choice19% == 2 goto desktop1

:virus
start
goto virus

:buglog
cls
echo Deel 0 bij 0 = Vorige oplossing
echo Opslaan
echo 1) Ga terug
set /p choice20=C:\

if %choice20% == 1 goto desktop1

:drawings
cls
echo Welkom bij Tekeningen
echo 1) Huis
echo 2) Go back
set /p choice21=C:\

if %choice21% == 1 goto housedrawing
if %choice21% == 2 goto desktop1
goto drawings

:housedrawing
cls
echo    /\
echo   /()\
echo  |̅̅̅̅|
echo  | [] |
echo  |    |
echo  | |͞͞|
echo  | |- |
echo  |_|__|
pause
goto drawings

:desktop5
cls
echo 1) DonderTeller
echo 2) Zaklamp
echo 3) Ga terug
set /p choice22=C:\

if %choice22% == 1 goto thundercounter
if %choice22% == 2 goto flashlight
if %choice22% == 3 goto desktop4

:thundercounter
echo Welkom bij DonderTeller
echo Hiermee kan je tellen hoever weg donder is.
echo Begin te tellen van de eerstvolgende donderslag.
echo Hoeveel seconden?
set /p ts=C:\
pause
set /a thunderdistance=340*%ts%
echo De donder is ongeveer %thunderdistance% meter weg van jou.
pause
goto desktop1

:flashlight
cls
color 07
echo Licht uit
pause
cls
color 70
echo Licht aan
pause
goto flashlight
