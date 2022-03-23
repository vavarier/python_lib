#!/bin/sh
echo "=> Browse to find old versions..."
FILE=/usr/lib/python3.10/moulitek
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
sudo mv moulitek_lib/moulitek /usr/lib/python3.10
rmdir moulitek_lib

tput setaf 2
echo "=> Repository_created"
tput sgr0

tput setab 2
echo "=> Installation Done"
tput sgr0
