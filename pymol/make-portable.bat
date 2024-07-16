if not defined PREFIX set PREFIX=%~dp0

:: fix Qt
set QT_CONF=%PREFIX%\qt.conf
echo [Paths] > "%QT_CONF%"
echo Prefix = ./Library >> "%QT_CONF%"
