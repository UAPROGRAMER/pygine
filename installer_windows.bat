set cdirrectory=%cd%
set pyginecpfrom=%cdirrectory%\pygine\
cd /D C:\
for /f %%i in ('python -m site --user-site') do set destenation=%%i
robocopy %pyginecpfrom% %destenation% /E