#!/bin/bash

#script that makes spellchecking between a file or stdin and a given dictionary

echo -n "If you want to check the mispelled words from a file, enter '1'. If you want to check the mispelled words from the stdin, enter '2' "
read mytext 

tr 'A-Z' 'a-z' < dict | uniq > lower_case_dict.txt

if [ "$mytext" == "1" ]; then
	echo "Enter the filename (example : tmpfile.txt)"
	read filename

	tr -sc [:alpha:] '\n' < "$filename" | tr A-Z a-z | sort | uniq | awk 'NF' | comm -23 - lower_case_dict.txt

else
	echo "Enter the text to be checked"
	read text

	echo "$text" >> temp_file.txt
	tr -sc [:alpha:] '\n' < temp_file.txt | tr A-Z a-z | sort | uniq | awk 'NF' | comm -23 - lower_case_dict.txt

fi
