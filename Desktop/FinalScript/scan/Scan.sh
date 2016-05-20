#!/bin/bash
ddir=$(pwd)"/*.txt";
for file in $ddir
do
  while read url
  do
    trap 'echo "Interrupted"; continue;' INT
    joomscan -u $url -ot;
    echo url;
    trap - INT
  done < "$file"
done
