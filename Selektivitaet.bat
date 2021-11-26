@echo off
color 0a
mode 50,20 
cls

echo ##################################################
echo #####Selektivität von Sicherungen bestimmen.#####
echo ##################################################

:a
python main.py
set /p x="Neustart (Y/N)"  
IF %x% == y goto a
IF %x% == Y goto a
exit