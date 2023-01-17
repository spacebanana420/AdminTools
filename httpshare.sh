#!/bin/bash

if [[ -e $1 ]]
echo "1. Move     2.Copy     3.Batch"
read operation
case operation in
1)
    mv -r "$1" /var/www/html/share
;;
2)
    cp -r "$1" /var/www/html/share
;;
3)
    echo "You need to choose a correct operation"
;;
*)
    echo "You need to choose a correct operation"
;;
esac
