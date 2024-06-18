@echo off

:choice
color 3B
title start
echo 1) English
echo 2) Nederlands
set /p language=C:\

if %language% == 1 goto en
if %language% == 2 goto nl
goto choice

:en
cls
echo 1) USA
echo 2) UK
set /p en=C:\

if %en% == 1 goto enus
if %en% == 2 goto enuk
if %en% == 1S goto enusS
if %en% == 2S goto enukS
goto en

:enus
cls
cd lang-en
start xanadaos_enus

:enuk
cd lang-en
start xanadaos_enuk

:enusS
cls
cd lang-en
start xanadaos_enus_safe

:enukS
cd lang-en
start xanadaos_enuk_safe

:nl
cls
echo 1) Belgie
set /p nl=C:\

if %nl% == 1 goto nlbe
if %nl% == 1S goto nlbe_safe
goto nl

:nlbe
cls
cd lang-nl
start xanadaos_nlbe

:nlbe_safe
cls
cd lang-nl
start xanadaos_nlbe_safe
