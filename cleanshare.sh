#!/bin/bash

echo "Server archive:"
ls /var/www/html/share
echo ""; echo "Are you sure you want to clean the server archive? (y/n)"
read answer
if [[ $answer == "y" || $answer == "yes"]]
then
  sudo rm -r /var/www/html/share/*
else
  echo "Operation cancelled"
fi
