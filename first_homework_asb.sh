#!/bin/bash
welcome="THANK YOU FOR USING OUR SCRIPT"

>&2 echo $welcome
>&2 echo "$1"
>&2 echo "$2"

>&0 echo "Using esearch..."

parametros=$(wget -q https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi/\?db\=$1\&term\="$2"\&usehistory\=y -O temp.fasta)

key=$(less temp.fasta |grep "<QueryKey>"|cut -d ">" -f 8-|cut -d "<" -f -2 |cut -d ">" -f 2-)  

webenv=$(less temp.fasta |grep "<WebEnv>"|cut -d ">" -f 10-|cut -d "<" -f -2|cut -d ">" -f 2-)

>&0 echo "Using efetch..."  

wget -q https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi/\?db\=$1\&query_key\=$key\&WebEnv\=$webenv\&rettype\=fasta -O- 

rm temp.fasta

>&0 echo "Done jedi knight"\ 
>&0 echo "Sincerely, young padawans" 

# Bernardo Augusto 2814
# Marcelo Pereira 2691
# Daniel Marçal 2675
