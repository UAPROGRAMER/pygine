set cdirrectory=%cd%
set pyginecpfrom=%cdirrectory%\pygine\
cd /D C:\
for /f %%i in ('python -m site --user-site') do set destenation=%%i
echo "copying pygine from %pyginecpfrom% to %destenation%"
robocopy %pyginecpfrom% %destenation% /E
echo "success"