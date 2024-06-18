cdirrectory=$PWD
pyginecpfrom="$cdirrectory/pygine/"
cd ~
echo "copying pygine from $pyginecpfrom to `python3 -m site --user-site`"
cp -r $pyginecpfrom "`python3 -m site --user-site`"
echo "success"