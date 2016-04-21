import sys

'''

File:cleanse_results.py
Author:cc
Date: April 12, 2016

Preconditions:
- there exists a data file named results.dat that contains structured data for parsing 
  (this currently arrives as a part of the shell script that curls siue's obits page
   and is archived along the way)
- there exists a master list of all past deaths all_deaths.dat that is read and writable
  in the cwd
- there exists a python script that will send an email to localhost?

Postconditions:
- the results.dat file is read and any new entries that are extracted from that raw data
  are added to all_deaths.dat
- An email is sent via smtp on localhost indicating that there were new deaths
'''

datafile='data/results.dat'
death_file='data/all_deaths.dat'



def get_existing_entries(dbfile):
   ''' Return a list data structure of existing entries contained in the dbfile '''
   already_dead = []
   with open(dbfile, 'r') as dfile:
      for x in dfile.readlines():
         already_dead.append(x.strip())
   return already_dead

def _parse_line_content(line):
   ''' A line currently formatted as follows:
       <h3 class="title"><a href="Mannix-James.shtml">Retired USAF Colonel James P. Mannix Sr., 1944-2016; Was Business Affairs Director</a></h3>
       is passed in and only the Retired USAF Colonel James P. Mannix Sr., 1944-2016; Was Business Affairs Director would be returned
   '''
   s1 = line.split('>')
   s2 = s1[2].split('<')
   return s2[0].strip()

def get_todays_entries(data_file_name):
   ''' Return a list data structure containing all of the entries for today's scrape '''
   todays_deaths = []
   with open(data_file_name, 'r') as fin:
      for line in fin.readlines():
         todays_deaths.append(_parse_line_content(line))
   return todays_deaths

def write_data_file(data, filename, mode='a'):
   with open(filename, mode) as dout:
      dout.write(data + '\n')

def main():
   existing_deaths = get_existing_entries(death_file)
   todays = get_todays_entries(datafile)
   for death in todays:
      if not death in existing_deaths:
         write_data_file(death, death_file)
         print("+++ " + death + " was added")
      else:
         print("=== " + death + " exists")        

if __name__ == '__main__':
   main()


