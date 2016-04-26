#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

current_year="$(date +"%Y")"

now="$(date +"%m-%d-%Y_%s")"

old="old_results_${now}.dat"

url="http://www.siue.edu/news/obituaries/${current_year}/index.shtml"

mv ${DIR}/data/results.dat data/${old}

curl ${url} | grep  -i -A 1 news_entry | grep title > ${DIR}/data/results.dat

python ${DIR}/cleanse_results.py

#curl ${url} > today.html
#diff -q today.html ${old} 
