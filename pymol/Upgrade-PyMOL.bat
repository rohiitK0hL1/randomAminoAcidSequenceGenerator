@echo upgrade pymol to the latest available version
@set PYTHONHOME=
@set PREFIX=%~dp0.
@call "%~dp0Scripts\activate.bat"

call conda install ^
  -p "%PREFIX%" ^
  "schrodinger::pymol"

@pause
