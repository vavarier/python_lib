#!/bin/sh
a=0
echo "=> Browse to find old versions..."
PYPATH=`python -c "import sys; print('\n'.join(sys.path))" | sed -n '3p'`
FILE=$PYPATH/moulitek
if [ -d $FILE ]
then
    echo "=> Erasing old repository..."
    sudo rm -rf $FILE
fi

if [ -f $FILE ]
then
    echo "=> Erasing old bin..."
    sudo rm -rf $FILE
fi

tput setaf 2
echo "=> Done cleaning"
tput sgr0


tput setaf 2
echo "=> Creating repository..."
tput sgr0

git clone git@github.com:vavarier/python_lib.git moulitek_lib
sudo mv moulitek_lib/lib/moulitek $PYPATH
rm -rf moulitek_lib

tput setaf 2
echo "=> Repository_created"
tput sgr0

tput setab 2
echo "=> Installation Done"
tput sgr0
