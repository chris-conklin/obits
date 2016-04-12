#!/bin/bash

current_year="$(date +"%Y")"

now="$(date +"%m-%d-%Y_%s")"

old="old_results_${now}.dat"

url="http://www.siue.edu/news/obituaries/${current_year}/index.shtml"

mv data/results.dat data/${old}

curl ${url} | grep  -i -A 1 news_entry | grep title > data/results.dat

python cleanse_results.py

#curl ${url} > today.html
#diff -q today.html ${old} 
