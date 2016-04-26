- Working with obituary data to create a data driven python application


$ ./check_obits.sh

1. Pulls raw html from the siue obituary page and extracts the desired obituary information via grep.
2. Calls cleanse_results.py which processes the new lines, checks them against existing lines and reports any difference. Thus, you are presented with an output of deaths for the current year with the details of their association. 


