REM Excluding this line, this code has 10674 characters.
@echo OFF
color 3B

:login
cls
title XANADA OS 1.0
echo Welcome to XANADA OS 1.0!
echo Made by Sapero before 2019
echo Do you want to login
echo 1) Yes
echo 2) No
set /p login0=C:\

if %login0% == 1 goto desktop1
if %login0% == 2 goto savecheck

:savecheck
echo Do you have a save?
echo 1) Yes
echo 2) No
set /p login1=C:\

if %login1% == 1 goto desktop1
if %login1% == 2 goto name

:name
cls
echo What is your name?
set /p name=C:\
goto age

:age
echo.
echo What is your age?
set /p age=C:\
goto dob

:dob
echo.
echo What is your Date of birth?
set /p dob=C:\
goto bc

:bc
echo.
echo What is the Country you are born in?
set /p bc=C:\
goto gender

:gender
echo.
echo What is your gender?
set /p gender=C:\
echo.
goto statsload

:statsload
cls
echo Name: %name%
echo Age: %age%
echo DOB: %dob%
echo Country of Birth: %bc%
echo Gender: %gender%
pause
goto desktop1

:start
echo.
echo Hello %name%!
echo Do you want to goto desktop?
echo 1) Yes
echo 2) No
set /p choice1=C:\

if %choice1% == 1 goto desktop1
if %choice1% == 2 exit

:desktop1
cls
color 3B
echo Welcome to the desktop. What do you want to do?
echo 1) Calculator
echo 2) Calendar
echo 3) Browser
echo 4) Memory
echo 5) Load Profile
echo 6) More
set /p choice2=C:\

if %choice2% == 1 goto calculator
if %choice2% == 2 goto calender
if %choice2% == 3 goto browser
if %choice2% == 4 goto memorystart
if %choice2% == 5 goto statsload
if %choice2% == 6 goto desktop2
goto desktop1

:calculator
cls
echo Welcome to Calculator! Only a 32-Bit basis.
echo Press 1 for Addition
echo Press 2 for Subtraction
echo Press 3 for Multiplication
echo Press 4 for Division
echo Press 5 to Quit
set /p type=

if %type%==1 goto add
if %type%==2 goto sub
if %type%==3 goto mul
if %type%==4 goto div
if %type%==5 goto desktop1
goto calculator

:add
echo.
echo Addition
echo Please choose the 2 numbers you wish to add
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
echo Subtraction
echo Please choose the 2 numbers you wish to subtract
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
echo Multiplication
echo Please choose the 2 numbers you wish to multiply
set /p num1=
set /p num2=
echo %num1%*%num2%?
pause
set /a Answer=%num1%*%num2%
echo %Answer%
pause
goto calculator

:div
echo Division
echo Please choose the 2 numbers you wish to divide
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
echo Welcome to Calendar!
echo Here you can see the date.
echo Date: %date% Time: %time%
pause
goto desktop1

:browser
cls
echo Welcome to Browser!
echo Here you can surf the Internet all the day!
echo Are you ready to start?
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
echo Welcome to Memory!
echo Do you want to start?
echo 1) Yes
echo 2) No
set /p choice4=C:\

if %choice4% == 1 goto memoryquestion
if %choice4% == 2 goto desktop1
goto memorystart

:memoryquestion
cls
echo You have the numbers:
echo 1) %random%
echo 2) %random%
echo 3) %random%
echo Are you ready?
pause
cls
echo Which number was number 2?
set /p choice5=C:\

if %choice5% == %number2% goto memorywin
if %choice5% == not %number2% goto memorywrong

:memorywin
cls
echo You are right!
echo You win the game!
pause
goto desktop1

:memorywrong
cls
echo You are wrong!
echo Retry
pause
goto memorystart

:desktop2
cls
echo 1) Shut down
echo 2) Restart
echo 3) Antivirus
echo 4) Write
echo 5) View File (only if you have written a file in Write)
echo 6) Back
echo 7) More
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
echo Are you sure you are gonna shut down?
echo 1) Yes
echo 2) No
set /p choice7=C:\

if %choice7% == 1 goto shutdown2
if %choice7% == 2 goto desktop1
goto shutdown1

:shutdown2
cls
echo Shutting down...
ping 10 9 8 7 6 5 4 3 2 1
exit

:restart1
cls
echo Are you sure you want to restart?
echo 1) Yes
echo 2) No
set /p choice8=C:\

if %choice8% == 1 goto restart2
if %choice8% == 2 goto desktop1
goto restart1

:restart2
cls
echo Restarting...
ping 10 9 8 7 6 5 4 3 2 1
goto login

:antivirus1
cls
echo Welcome to XANADA Antivirus
if exist virus.exe goto antivirusvirus
if not exist virus.exe goto antivirusnone

:antivirusvirus
echo.
echo Warning! Virus detected!
pause
del virus.exe
goto desktop1

:antivirusnone
echo.
echo Your computer is secure!
pause
goto desktop1

:write1
cls
echo Welcome to Write!
echo Here you can write documents.
echo Do you want to create a new file?
echo 1) Yes
echo 2) No
set /p choice9=C:\

if %choice9% == 1 goto write2
if %choice9% == 2 goto desktop1
goto write1

:write2
cls
echo How do you want to name your file?
set /p filename=C:\
echo What text do you want to have in your document?
set /p text=C:\
echo File created!
echo To view your file choose "View documents" on The Desktop.
pause
goto desktop1

:viewwrite1
cls
echo Welcome to View Documents!
echo Your documents:
echo 1) %filename%
echo Do you want to view your file?
echo 1) Yes
echo 2) No
set /p choice10=C:\

if %choice10% == 1 goto viewwrite2
if %choice10% == 2 goto desktop1

:viewwrite2
cls
echo File name:
echo %filename%
echo Text:
echo %text%
pause
goto desktop1

:desktop3
cls
echo 1) Quiz
echo 2) Zombie Fight
echo 3) Matrix
echo 4) Go back
echo 5) More
set /p choice11=C:\

if %choice11% == 1 goto quiz
if %choice11% == 2 goto zombiefight
if %choice11% == 3 goto matrix
if %choice11% == 4 goto desktop2
if %choice11% == 5 goto desktop4
goto desktop3

:quiz
cls
echo OK then, first question. How many countries are in the UK?
set /p choice12=Enter-
if %choice12% == 3 goto quizanswerright
if %choice12% == 4 goto quizanswermisconception1
if %choice12% == 2 goto quizanswermisconception2
cls
echo Wrong! No where near!
echo Go back = 1
set /p choice12=Enter-
if %choice12% == 1 goto quiz

:quizanswerright
cls
echo You are a legend mate! Northern Ireland is just a province! Sorry that was a bit of a trick question.
pause
goto desktop1

:quizanswermisconception1
cls
echo Ehhh... Close. That is a misconseption. There is not '4' countries in the UK. Northern Ireland is a province.
echo Try Again = 1
set /p choice13=Enter-
if %choice13% == 1 goto quiz
cls
echo Can you choose one of the numbers there please? That would be a REAL help.
echo Go back = 1
set /p choice13=Enter-
if %choice13% == 1 goto quizanswermisconception1

:quizanswermisconception2
cls
echo Ehhh... Close. That is a misconseption. There is not '2' countries in the UK. Great Britain is an island, not a country!
echo Try Again = 1
set /p choice14=Enter-
if %choice14% == 1 goto quiz
cls
echo Can you choose one of the numbers there please? That would be a REAL help.
echo Go back = 1
set /p choice14=Enter-
if %choice14% == 1 goto quizanswermisconception2

:zombiefight
cls
echo Oh no, a zombie comes to you!
echo What will you do?
echo 1) Punch
echo 2) Kick
set /p choice15=C:\

if %choice15% == 1 goto punch
if %choice15% == 2 goto kick
goto zombiefight

:punch
echo You used Punch!
echo Zombie used Bite!
echo Your life is now: 7
echo Enemy's life is now: 3
echo What will you use?
echo 1) Kick
set /p choice16=C:\

if %choice16% == 1 goto zombiekill
goto punch

:kick
echo You used Kick!
echo Zombie used Bite!
echo Your life is now: 7
echo Enemy's life is now: 5
echo What will you use?
echo 1) Punch
set /p choice17=C:\

if %choice17% == 1 goto zombiekill
goto kick

:zombiekill
cls
echo Congratulations!
echo You killed the zombie!
pause
goto desktop1

:matrix
@echo off
color 0a
echo %random%%random%%random%%random%%random%%random%%random%%random%%random%%random%%random%
goto matrix

:desktop4
cls
echo 1) Open Apps
echo 2) Virus
echo 3) Clicker
echo 4) Bugs
echo 5) Drawings
echo 6) Go back
echo 7) More
set /p choice18=C:\

if %choice18% == 1 goto openapps
if %choice18% == 2 goto virus
if %choice18% == 3 start xanadaclicker_enus.vbs
if %choice18% == 4 goto buglog
if %choice18% == 5 goto drawings
if %choice18% == 6 goto desktop3
if %choice18% == 7 goto desktop5
goto desktop4

:openapps
cls
echo 1) Notepad
echo 2) Go back
set /p choice19=C:\

if %choice19% == 1 start notepad.exe
if %choice19% == 2 goto desktop1

:virus
start
goto virus

:buglog
cls
echo Divide 0 by 0 = Previous solution
echo Saving
echo 1) Go back
set /p choice20=C:\

if %choice20% == 1 goto desktop1

:drawings
cls
echo Welcome to Drawings
echo 1) House
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
echo 1) ThunderCounter
echo 2) Flashlight
echo 3) Go Back
set /p choice22=C:\

if %choice22% == 1 goto thundercounter
if %choice22% == 2 goto flashlight
if %choice22% == 3 goto desktop4

:thundercounter
echo Welcome to ThunderCounter
echo You can count the distance of thunder.
echo Count from the first thunder
echo How many seconds?
set /p ts=C:\
pause
set /a thunderdistance=340*%ts%
echo The thunder is about %thunderdistance% metres away from you.
pause
goto desktop1

:flashlight
cls
color 07
echo Light off
pause
cls
color 70
echo Light on
pause
goto flashlight
